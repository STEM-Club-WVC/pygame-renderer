'''
Created by: Michael Duffy

Created: 29 October 2019

Credit for original code to: DLC Energy (Youtube username)

Youtube Link to Video: https://www.youtube.com/watch?v=g4E9iq0BixA&t=772s

'''
import pygame, sys, math

w, h = 400, 400; cx, cy = w//2, h//2

def rotate2d(pos, rad):

    x, y = pos

    s,c = math.sin(rad),math.cos(rad)

    return x*c-y*s, y*c+x*s


class Cam:

    def __init__(self, pos = (0,0,0), rot = (0,0)):

        self.pos = list(pos)
        self.rot = list(rot)

    def events(self, event):

        if(event.type == pygame.MOUSEMOTION):

            x, y = event.rel; x /= 1000; y /= 1000

            self.rot[0] += y; self.rot[1] += x


    def update(self, dt, key):

        s = dt/100

        if key[pygame.K_q]: self.pos[1] += s
        if key[pygame.K_e]: self.pos[1] -= s

        x, y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])

        if(key[pygame.K_w]): self.pos[0] += x; self.pos[2] += y
        if(key[pygame.K_s]): self.pos[0] -= x; self.pos[2] -= y
        if(key[pygame.K_a]): self.pos[0] -= y; self.pos[2] += x
        if(key[pygame.K_d]): self.pos[0] += y; self.pos[2] -= x

        if(key[pygame.K_ESCAPE]): pygame.quit(); sys.exit()


class Cube:

    vertices = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
                (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
                ]

    faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6),
             (0, 3, 7, 4), (1, 2, 6, 5)
             ]

    colors = [(0, 0, 0), (255, 0, 0), (255, 255, 0), (255, 255, 255),
              (120, 30, 255), (0, 255, 0)
              ]

    def __init__(self, pos = (0,0,0), dims = (0,0,0), scale = 1, type = "cube"):

        '''

        x,y,z = pos

        self.verts = [(x + X / 2,y + Y / 2,z + Z / 2) for X,Y,Z in self.vertices]

        '''

        scale = 1/scale

        w, l, h = dims

        x, y, z = pos

        if(type == 'cube'):

            self.verts = [((x + X / 2) / scale, (y + Y / 2) / scale, (z + Z / 2) / scale)
                          for X, Y, Z in self.vertices
                          ]


pygame.init()
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

cam = Cam((0,0,-5))

pygame.event.get(); pygame.mouse.get_rel()
pygame.mouse.set_visible(0); pygame.event.set_grab(1)

cubes = [Cube((0,1,0), scale = 100), Cube((2,0,0)), Cube((-2,0,0))]

while True:

    dt = clock.tick(100)

    for event in pygame.event.get():

        if event.type == pygame.QUIT: pygame.quit(); sys.exit()

        try: cam.events(event)

        except: pass

    screen.fill((0,0,200))

    face_list = []; face_color = []; depth = []

    for obj in cubes:

        vert_list = []; screen_coords = []; colors = []

        for x,y,z in obj.verts:

            x -= cam.pos[0]; y -= cam.pos[1]; z -= cam.pos[2]

            x, z = rotate2d((x,z), cam.rot[1])
            y, z = rotate2d((y,z), cam.rot[0])

            vert_list += [(x,y,z)]

            f = 200 / z
            x, y = x * f, y * f

            screen_coords += [(cx + int(x), cy + int(y))]


        for f in range(0, len(obj.faces)):

            face = obj.faces[f]

            on_screen = False

            for i in face:

                if(vert_list[i][2] > 0 and w//2 > x > -w//2 and h//1.75 > y > -h//1.75):

                    on_screen = True

                    break


            if(on_screen == True):

                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [obj.colors[f]]

                depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(0, 3))]

        # Final drawing part, all faces from all objects
        order = sorted(range(len(face_list)), key = lambda i:depth[i], reverse = True)
        for i in order:

            try:
                pygame.draw.polygon(screen, face_color[i], face_list[i])

            except:

                pass


    pygame.display.flip()

    key = pygame.key.get_pressed()
    cam.update(dt, key)