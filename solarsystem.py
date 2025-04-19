#provides imports for things like exit program for a condition
import sys
#allows the ability to use functions like sin and cosine 
import math
#used in multimedia and game(i made this act like a game)
import pygame
#numpy allows for working with arrays and matrices
import numpy as np
#This import allows for actions coming from pygame.locals( alllowing OPENGL and QUIT)
from pygame.locals import *
#the next two imports allows us to use 3D graphics rendering
from OpenGL.GL import *
from OpenGL.GLU import *

'''
loads image using pygame
coverts to pixel data
creates a new OpenGL texture for use 
uploads texture data to open GL
'''
def load_texture(filename):
    surface = pygame.image.load(filename).convert_alpha()
    texture_data = pygame.image.tostring(surface, "RGBA", 1)
    width = surface.get_width()
    height = surface.get_height()

    texid = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texid)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    return texid
'''
Creates a helper function for drawing spheres(quadric)
enables texture mapping
binds the texture to objects
draws textured sphere with a radius given(defined later)
Deletes the quaadric later 
'''
def draw_sphere(radius, texture):
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    glBindTexture(GL_TEXTURE_2D, texture)
    gluSphere(quadric, radius, 32, 32)
    gluDeleteQuadric(quadric)

'''
returns a 4x4 matrix to help transform sphere in 3D in real time
'''
def translation_matrix(dx, dy, dz):
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1 ]
    ], dtype=np.float32)

'''
returns a 4x4 matrix to help with the rotations around the sun
'''
def rotation_matrix_y(degrees):
    radians = math.radians(degrees)
    cos_a = math.cos(radians)
    sin_a = math.sin(radians)
    return np.array([
        [ cos_a, 0, sin_a, 0],
        [ 0,     1, 0,     0],
        [-sin_a, 0, cos_a, 0],
        [ 0,     0, 0,     1]
    ], dtype=np.float32)

#combines Y-axis rotation into transformations matrix to calculate real time rot
def combine_transformations(rotation_deg, tx, ty, tz):
    R = rotation_matrix_y(rotation_deg)
    T = translation_matrix(tx, ty, tz)
    # Note: matrix multiplication order matters (rotation then translation)
    return np.dot(R, T)


#init:pygame and create OpenGL window
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL| RESIZABLE)
    
    # Enable depth testing and texture mapping
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    
    # Set up perspective projection
    gluPerspective(45, (display[0] / display[1]), 0.1, 1000.0)
    #move scam back for perspective
    glTranslatef(0.0, 0.0, -90)  

    
    # Load textures for the Sun and Earth
    star_texture=load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\star.jpg")
    sun_texture = load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\sun.png")
    earth_texture = load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\earth.jpg")
    mercury_texture = load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\mercury.jpg")
    venus_texture = load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\venus.jpg")
    mars_texture = load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\mars.jpg")
    jupiter_texture = load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\jupiter.jpg")
    saturn_texture = load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\saturn.png")
    saturn_ring_texture = load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\saturnring.png")
    uranus_texture = load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\uranus.jpg")
    neptune_texture = load_texture(r"C:\Users\lawre\Desktop\Baldwin Wallace Spring 2025\Linear Algebra\Final Project\neptune.jpg")
    # Orbit parameters for Earth (scaled for visualization)
    earth_orbit_radius = 20.0  # Distance from Sun
    earth_orbit_speed = 0.3    # Degrees per frame
    earth_angle = 0.0          # Starting angle
    #Mercury Parameters
    mercury_orbit_radius = 10.0
    mercury_orbit_speed = 1.2
    mercury_angle = 0.0
    #venus parameters
    venus_orbit_radius = 15.0
    venus_orbit_speed = 1.2
    venus_angle = 0.0
    #mars parameters
    mars_orbit_radius = 26.0
    mars_orbit_speed = 0.24
    mars_angle = 0.0
    #Jupiter paramters
    jupiter_orbit_radius = 35.0
    jupiter_orbit_speed = 0.13
    jupiter_angle = 0.0
     #Saturn paramters
    saturn_orbit_radius = 45.0
    saturn_orbit_speed = 0.09
    saturn_angle = 0.0
    #Uranus paramters
    uranus_orbit_radius = 55.0
    uranus_orbit_speed = 0.06
    uranus_angle = 0.0
    #Neptune paramters
    neptune_orbit_radius = 65.0
    neptune_orbit_speed = 0.045
    neptune_angle = 0.0

    clock = pygame.time.Clock()

    # Main loop
    while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                
                elif event.type == VIDEORESIZE:
                    width, height = event.size
                    if height ==0:
                        height = 1
                    
                    glViewport(0, 0, width, height)
                    glMatrixMode(GL_PROJECTION)
                    glLoadIdentity()
                    gluPerspective(45, (width / height), 0.1, 1000.0)
                    glMatrixMode(GL_MODELVIEW)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
    # Draw the background sphere
        
            glPushMatrix()
            glDisable(GL_DEPTH_TEST)
            glDisable(GL_LIGHTING)

            glEnable(GL_CULL_FACE)          
            glCullFace(GL_FRONT)            

            glBindTexture(GL_TEXTURE_2D, star_texture)
            quadric = gluNewQuadric()
            gluQuadricTexture(quadric, GL_TRUE)
            gluSphere(quadric, 500, 64, 64)
            gluDeleteQuadric(quadric)

            glDisable(GL_CULL_FACE)         
            glEnable(GL_DEPTH_TEST)
            glEnable(GL_LIGHTING)
            glPopMatrix()
                
                #enable sunlight

            # Enable lighting and a basic light source
            glEnable(GL_LIGHTING)
            glEnable(GL_LIGHT0)

            # Position the light at the Sun’s location
            light_position = [0.0, 0.0, 0.0, 1.0]
            glLightfv(GL_LIGHT0, GL_POSITION, light_position)

            # Brighter ambient and diffuse light
            glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
            glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.2, 1.2, 1.2, 1.0])
            glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

            # Optional: make materials reflect the light well
            glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
            glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
            glMaterialf(GL_FRONT, GL_SHININESS, 50.0)
                
                # ---------------------------
                # Draw the Sun at the center
                # ---------------------------
            glPushMatrix()
            glDisable(GL_LIGHTING)  # Don't apply lighting to the Sun — it's the light source
            glColor3f(1.0, 1.0, 1.0)
            draw_sphere(5, sun_texture)
            glEnable(GL_LIGHTING)   # Re-enable lighting for the rest
            glPopMatrix()

                # ---------------------------
                # Draw  saturn orbiting the Sun using our linear algebra transformations
                # ---------------------------
            saturn_transform = combine_transformations(saturn_angle, saturn_orbit_radius, 0, 0)

            glPushMatrix()
            glMultMatrixf(saturn_transform.T)
            draw_sphere(1.9, saturn_texture)  
            
            # ---------------------------
            # Saturn orbiting the Sun
            # ---------------------------
            saturn_angle = (saturn_angle + saturn_orbit_speed)%360
            # ---------------------------
            # Draw the ring (keep it inside Saturn's transform)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glBindTexture(GL_TEXTURE_2D, saturn_ring_texture)
            glBegin(GL_QUADS)

            ring_size = 6.0  # Outer size
            glTexCoord2f(0, 0); glVertex3f(-ring_size, 0, -ring_size)
            glTexCoord2f(1, 0); glVertex3f(ring_size, 0, -ring_size)
            glTexCoord2f(1, 1); glVertex3f(ring_size, 0, ring_size)
            glTexCoord2f(0, 1); glVertex3f(-ring_size, 0, ring_size)
            glEnd()
            glDisable(GL_BLEND)
            glPopMatrix()
            # ---------------------------
            # Draw  jupiter orbiting the Sun using our linear algebra transformations
            # ---------------------------
            jupiter_transform = combine_transformations(jupiter_angle, jupiter_orbit_radius, 0, 0)

            glPushMatrix()
            glMultMatrixf(jupiter_transform.T)
            draw_sphere(1.9, jupiter_texture)  
            glPopMatrix()
            # ---------------------------
            # Jupiter orbiting the Sun
            # ---------------------------
            jupiter_angle = (jupiter_angle + jupiter_orbit_speed)%360
            # ---------------------------
            # Draw  Mars orbiting the Sun using our linear algebra transformations
            # ---------------------------
            mars_transform = combine_transformations(mars_angle, mars_orbit_radius, 0, 0)

            glPushMatrix()
            glMultMatrixf(mars_transform.T)
            draw_sphere(1.9, mars_texture)  
            glPopMatrix()
            # ---------------------------
            # mars orbiting the Sun
            # ---------------------------
            mars_angle = (mars_angle + mars_orbit_speed)%360
            # ---------------------------
            # Draw  venus orbiting the Sun using our linear algebra transformations
            # ---------------------------
            venus_transform = combine_transformations(venus_angle, venus_orbit_radius, 0, 0)

            glPushMatrix()
            glMultMatrixf(venus_transform.T)
            draw_sphere(1.9, venus_texture)  # Slightly smaller than Earth
            glPopMatrix()
            # ---------------------------
            # venus orbiting the Sun
            # ---------------------------
            venus_angle = (venus_angle + venus_orbit_speed)%360
                # Draw  uranus orbiting the Sun using our linear algebra transformations
            # ---------------------------
            uranus_transform = combine_transformations(uranus_angle, uranus_orbit_radius, 0, 0)

            glPushMatrix()
            glMultMatrixf(uranus_transform.T)
            draw_sphere(2.2, uranus_texture)  # Slightly smaller than Earth
            glPopMatrix()
            # ---------------------------
            # uranus orbiting the Sun
            # ---------------------------
            uranus_angle = (uranus_angle + uranus_orbit_speed)%360



            # Draw  neptune orbiting the Sun using our linear algebra transformations
            # ---------------------------
            neptune_transform = combine_transformations(neptune_angle, neptune_orbit_radius, 0, 0)
            glPushMatrix()
            glMultMatrixf(neptune_transform.T)
            draw_sphere(2.2, neptune_texture)  # Slightly smaller than Earth
            glPopMatrix()
            # ---------------------------
            # neptune orbiting the Sun
            # ---------------------------
            neptune_angle = (neptune_angle + neptune_orbit_speed)%360


            # Draw  Mercury orbiting the Sun using our linear algebra transformations
            # ---------------------------
            # Mercury orbiting the Sun
            mercury_angle = (mercury_angle + mercury_orbit_speed)%360

            mercury_transform = combine_transformations(mercury_angle, mercury_orbit_radius, 0, 0)
            glPushMatrix()
            glMultMatrixf(mercury_transform.T)
            draw_sphere(0.5, mercury_texture)  # Mercury is small
            glPopMatrix()
            

            # ---------------------------
            # Draw the Earth orbiting the Sun using our linear algebra transformations
            # ---------------------------
            earth_angle = (earth_angle + earth_orbit_speed) % 360
            # Build the transformation matrix:
            # First, rotate the Earth around the Y-axis, then translate it along the X-axis.
            transform = combine_transformations(earth_angle, earth_orbit_radius, 0, 0)

            glPushMatrix()
            # Load our custom transformation matrix.
            # We transpose it because OpenGL expects column-major order.
            glMultMatrixf(transform.T)
            # Optionally, to spin the Earth on its own axis, you could multiply another rotation here.
            draw_sphere(2, earth_texture)  # Earth with radius 2
            glPopMatrix()

            pygame.display.flip()

            clock.tick(60)  # Limit to 60 FPS


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", e)
        import traceback
        traceback.print_exc()
        pygame.quit()