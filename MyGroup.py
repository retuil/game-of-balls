import pygame


class MyGroup(pygame.sprite.Group):
    def check_any_click(self, mouse_pos):
        for sprite in self.sprites():
            click = sprite.check_click_button(mouse_pos)
            if click[0]:
                return click
        return False, False
