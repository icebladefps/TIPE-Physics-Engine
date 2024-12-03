import pygame as pg
from GraviPy.Visualize.Events.quit import quit
from GraviPy.Visualize.Events.viewport_scroll_zoom import viewport_scroll_zoom
from GraviPy.Visualize.Events.viewport_drag_state import viewport_drag_state
from GraviPy.Visualize.Events.viewport_drag import viewport_drag
from GraviPy.Visualize.Events.update_screen_size import update_screen_size
from GraviPy.Visualize.Events.viewport_drag_state import viewport_drag_state
from GraviPy.Visualize.Events.viewport_drag import viewport_drag
from GraviPy.Visualize.Events.update_screen_size import update_screen_size
from GraviPy.Visualize.Events.playpausespacebar import playpausespacebar

def EventHandler(viz, event):
    """
    Handles various events for the visualization.

    Parameters:
    - viz: The visualization object.
    - event: The event object representing the user input.

    Returns:
    None
    """

    if event.type == pg.QUIT:
       quit(viz)
        
    #check for scroll and adjust simulation width and height
    if event.type == pg.MOUSEBUTTONDOWN:
        viewport_scroll_zoom(viz, event)
            
    #check for click and drag to move simulation
    if event.type == pg.MOUSEBUTTONDOWN:
        viewport_drag_state(viz, event)

    if event.type == pg.MOUSEBUTTONUP:
        viewport_drag_state(viz, event)


    if event.type == pg.MOUSEMOTION:
        viewport_drag(viz, event)

    if event.type == pg.VIDEORESIZE:
        update_screen_size(viz, event)

    if  (event.type == pg.K_LSHIFT):
        #print("Shift pressed")
        viewport_drag_state(viz, event)
        
    #spacebar to play/pause
    if event.type == pg.KEYDOWN:
        playpausespacebar(viz, event)




