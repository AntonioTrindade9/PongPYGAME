import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#Raquete do jogador-------------------------------------------
class Raquete:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 100, 150)

    def mover(self, keys):
        if keys[pygame.K_w]: self.y -= 5
        if keys[pygame.K_s]: self.y += 5
        self.y = max(0, min(self.y, 600 - 150))
        self.rect.topleft = (self.x, self.y)

    def desenhar(self, screen):
        pygame.draw.rect(screen, "red", self.rect)
#Raquete do adversário------------------------------------------
class Inimigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 100, 150)

    def mover(self, ybola):
        self.y = ybola - 75
        self.y = max(0, min(self.y, 600 - 150))
        self.rect.topleft = (self.x, self.y)

    def desenhar(self, screen):
        pygame.draw.rect(screen, "blue", self.rect)
#Bola------------------------------------------------------------------
class Bola:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.vel_x = -3
        self.vel_y = -3
        self.raio = 30
        self.rect = pygame.Rect(self.x - 30, self.y - 30, 60, 60)

    def atualizar(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.rect.topleft = (self.x - self.raio, self.y - self.raio)

    def desenhar(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.raio)

jogador = Raquete(30, 50)
inimigo = Inimigo(650, 50)
bola = Bola()
chao = pygame.Rect(0, 550, 800, 50)
teto = pygame.Rect(0, 0, 800, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")

    keys = pygame.key.get_pressed()
    jogador.mover(keys)
    inimigo.mover(bola.y)
    bola.atualizar()

    # colisões
    if jogador.rect.colliderect(bola.rect):
        bola.vel_x = abs(bola.vel_x)
    if inimigo.rect.colliderect(bola.rect):
        bola.vel_x = -abs(bola.vel_x)
    if teto.colliderect(bola.rect):
        bola.vel_y = abs(bola.vel_y)
    if chao.colliderect(bola.rect):
        bola.vel_y = -abs(bola.vel_y)

    jogador.desenhar(screen)
    inimigo.desenhar(screen)
    bola.desenhar(screen)
    pygame.draw.rect(screen, "yellow", chao)
    pygame.draw.rect(screen, "yellow", teto)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
