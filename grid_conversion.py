import json
import re

sample_solutions = {
    3: '''[[0 1 1]
 [1 0 1]
 [1 1 0]]
''',
    4: '''[[0 1 1 0]
 [1 0 0 1]
 [1 0 0 1]
 [0 1 1 0]]
''',
    5: '''[[1 0 1 0 0]
 [0 1 0 0 1]
 [0 0 0 1 1]
 [1 1 0 0 0]
 [0 0 1 1 0]]
''',
    6: '''[[1 0 0 1 0 0]
 [0 0 1 1 0 0]
 [1 0 0 0 0 1]
 [0 0 0 0 1 1]
 [0 1 1 0 0 0]
 [0 1 0 0 1 0]]
''',
    7: '''[[0 0 0 1 0 1 0]
 [0 0 1 0 1 0 0]
 [1 0 0 0 0 0 1]
 [0 1 0 0 0 1 0]
 [1 0 0 0 0 0 1]
 [0 0 1 0 1 0 0]
 [0 1 0 1 0 0 0]]
''',
    8: '''[[0 0 1 0 1 0 0 0]
 [1 0 0 0 0 1 0 0]
 [0 0 0 0 1 0 0 1]
 [1 0 0 0 0 0 1 0]
 [0 1 0 0 0 0 0 1]
 [0 0 0 1 0 0 1 0]
 [0 1 1 0 0 0 0 0]
 [0 0 0 1 0 1 0 0]]
''',
    9: '''[[0 0 0 1 1 0 0 0 0]
 [0 1 0 0 0 0 1 0 0]
 [0 1 0 1 0 0 0 0 0]
 [0 0 0 0 0 0 1 0 1]
 [1 0 0 0 0 0 0 0 1]
 [1 0 1 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 1 0]
 [0 0 1 0 0 0 0 1 0]
 [0 0 0 0 1 1 0 0 0]]
''',
    10: '''[[0 0 0 0 1 0 1 0 0 0]
 [0 0 1 1 0 0 0 0 0 0]
 [0 0 0 0 0 0 1 0 0 1]
 [1 0 0 0 1 0 0 0 0 0]
 [0 1 0 0 0 0 0 0 0 1]
 [0 0 0 0 0 0 0 1 1 0]
 [1 1 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 1 0 0]
 [0 0 1 1 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 0 1 0]]
''',
    11: '''[[0 0 0 0 1 1 0 0 0 0 0]
 [0 0 0 0 0 0 0 1 0 1 0]
 [0 0 0 0 1 0 0 1 0 0 0]
 [0 0 0 0 0 0 0 0 0 1 1]
 [1 1 0 0 0 0 0 0 0 0 0]
 [0 0 1 0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 0 0 1 0 1]
 [1 1 0 0 0 0 0 0 0 0 0]
 [0 0 0 1 0 0 1 0 0 0 0]
 [0 0 1 1 0 0 0 0 0 0 0]
 [0 0 0 0 0 1 1 0 0 0 0]]
''',
    12: '''[[0 0 1 0 1 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 1 0 0 0 0 0]
 [0 0 0 0 0 0 0 1 0 1 0 0]
 [1 0 0 0 0 1 0 0 0 0 0 0]
 [0 0 1 0 1 0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 0 0 0 0 1]
 [0 0 0 0 0 0 0 1 0 1 0 0]
 [0 0 0 0 0 0 0 0 0 0 1 1]
 [0 1 0 1 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 0 1 0 0 0]
 [0 0 0 0 0 0 1 0 1 0 0 0]
 [0 0 0 1 0 0 0 0 0 0 1 0]]'''
}

def parse_grid_string(grid_str):
    """Parse a grid string into a 2D list of integers."""
    # Remove the outer brackets and split by lines
    lines = grid_str.strip().strip('[]').split('\n')
    grid = []
    for line in lines:
        # Extract numbers from each line using regex
        numbers = re.findall(r'\d+', line.strip())
        if numbers:  # Only add non-empty lines
            grid.append([int(n) for n in numbers])
    return grid

def grid_to_coordinates(grid):
    """Convert a 2D grid to coordinate format (x,y) where 1s become coordinates."""
    coordinates = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                coordinates.append((x, y))
    return coordinates

def coordinates_to_string(coordinates):
    """Convert coordinate list to the format expected by the HTML import."""
    return ';'.join(f'({x},{y})' for x, y in coordinates)

def convert_all_solutions():
    """Convert all sample solutions to coordinate format."""
    converted = {}
    
    for size, grid_str in sample_solutions.items():
        try:
            grid = parse_grid_string(grid_str)
            coordinates = grid_to_coordinates(grid)
            coord_string = coordinates_to_string(coordinates)
            converted[size] = coord_string
            print(f"Size {size}: {coord_string}")
        except Exception as e:
            print(f"Error converting size {size}: {e}")
    
    return converted

def main():
    """Main function to convert solutions and save to JSON."""
    print("Converting sample solutions to coordinate format...")
    converted_solutions = convert_all_solutions()
    
    # Save to JSON file
    output_file = 'sample_solutions.json'
    with open(output_file, 'w') as f:
        json.dump(converted_solutions, f, indent=2)
    
    print(f"\nConversion complete! Results saved to {output_file}")
    return converted_solutions

if __name__ == "__main__":
    main()

