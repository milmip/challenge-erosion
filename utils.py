def img2ascii(img_data, black='.', white='#') -> str:
    img_ascii = ''
    for line in img_data:
        for pixel in line:
            if pixel:
                img_ascii += white
            else:
                img_ascii += black
        img_ascii += '\n'

    return img_ascii[:-1]


def load_pbm(filename):
    instructions = []
    with open(filename, 'r') as file:
        for instruction in file:
            if instruction[0] != '#':
                instructions.append(instruction.replace('\n', ''))
    
    if instructions[0] != 'P1':
        print('Error')
        exit()
    
    width, height = int(instructions[1].split(' ')[0]), int(instructions[1].split(' ')[1])

    img_string = ''
    for line in instructions[2:]:
        img_string += line
    
    img_data = [None] * height

    for i in range(height):
        img_data[i] = [int(pixel) for pixel in list(img_string[i*width:(i+1)*width])]

    
    return img_data


def erosion(img, n):

    width = len(img[0])
    height = len(img)
    
    def iter():
        new_img = [[0 for i in range(width)] for j in range(height)]

        for i in range(height) :
            for j in range(width):
                if i ==  0 or i == height - 1 or j == 0 or j == width - 1:
                    continue

                if img[i+1][j] and img[i][j+1] and img[i-1][j] and img[i][j-1]:
                    new_img[i][j] = 1
        return new_img
    
    for _ in range(n):
        img = iter()
    
    return img
