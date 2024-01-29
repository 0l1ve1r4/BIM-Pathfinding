import matplotlib.pyplot as plt

def show_3DPlot(matrix: list) -> None:
    """ Plot 3D matrix

    Args:
        matrix List[List[List[int]]]: Each list inside the matrix represents a floor (which is also a matrix).
    """
    
    # Define color and z-axis mapping
    color_mapping = {
        0: 'white',
        1: 'black',
        2: 'red',
        3: 'green',
        4: 'darkgray',
        5: 'lightgray',
        6: 'yellow'
    }
    
    z_mapping = {
        0: -1.0,
        1: 0.4,
        2: 0.3,
        3: 0.3,
        4: 0.2,
        5: 0.2,
        6: 0.3
    }
    
    # Create figure and 3D axis
    fig = plt.figure(dpi=128)
    ax = fig.add_subplot(111, projection='3d')
    
    # Iterate through the matrix and plot each element
    for z in range(len(matrix)):
        if z > 0:
            z_mapping.update({0: 0.1})
           
        # Extract matrix dimensions
        rows = len(matrix[z])
        cols = len(matrix[z][0])
        
        for y in range(0, rows):  # Use stride to skip every second row
            for x in range(0, cols):  # Use stride to skip every second column
                color_index = matrix[z][y][x]
                if color_index in color_mapping:
                    color = color_mapping[color_index]
                    height = z_mapping.get(color_index, 0)
                        
                    ax.bar3d(x, y, z, 1, 1, height, color=color, shade=True)

    # Set axis labels
    # Set default elevation and azimuth
    ax.view_init(elev=45, azim=-50)
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')

    # Show the plot
    plt.show()