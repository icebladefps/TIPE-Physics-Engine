from GraviPy.Visualize.pygametoxy import pygame_to_xy

import pygame as pg
def viewport_scroll_zoom(viz, event):
    """
    Adjusts the size viewport of the visualization based on the mouse scroll event.

    Args:
        viz (Visualization): The visualization object.
        event (pygame.event.Event): The mouse scroll event.

    Returns:
        None
    """
    # Get the current mouse position
    current_pos = pg.mouse.get_pos()

    # Convert the mouse position to simulation coordinates
    sim_x, sim_y = pygame_to_xy(viz, current_pos[0], current_pos[1])

    # Calculate the zoom scale
    zoomfactor = 0.02

    if event.button == 4:  # If the mouse wheel is scrolled up
        viz.simulationwidth = [sim_x - (sim_x - viz.simulationwidth[0]) * (1 - zoomfactor), sim_x + (viz.simulationwidth[1] - sim_x) * (1 - zoomfactor)]
        viz.simulationheight = [sim_y - (sim_y - viz.simulationheight[0]) * (1 - zoomfactor), sim_y + (viz.simulationheight[1] - sim_y) * (1 - zoomfactor)]
    elif event.button == 5:  # If the mouse wheel is scrolled down
        viz.simulationwidth = [sim_x - (sim_x - viz.simulationwidth[0]) * (1 + zoomfactor), sim_x + (viz.simulationwidth[1] - sim_x) * (1 + zoomfactor)]
        viz.simulationheight = [sim_y - (sim_y - viz.simulationheight[0]) * (1 + zoomfactor), sim_y + (viz.simulationheight[1] - sim_y) * (1 + zoomfactor)]