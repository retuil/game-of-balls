import pygame


class MyGroup(pygame.sprite.Group):
    def check_any_click(self, mouse_pos):
        for sprite in self.sprites():
            if sprite.check_click_button(mouse_pos):
                return 1
                break
        return 0