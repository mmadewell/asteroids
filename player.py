from circleshape import *
from constants import *
from shot import *
import pygame

class Player(CircleShape):
    shot_cooldown_timer = 0

    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        if self.shot_cooldown_timer > 0:
            self.shot_cooldown_timer -= dt
        elif self.shot_cooldown_timer < 0:
            self.shot_cooldown_timer = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE] and self.shot_cooldown_timer <= 0:
            self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = (pygame.Vector2(0, 1) * PLAYER_SHOOT_SPEED)
        shot.velocity = shot.velocity.rotate(self.rotation)