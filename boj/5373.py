"""
큐빙
https://www.acmicpc.net/problem/5373
"""
import sys
input = sys.stdin.readline


class Cube:
    #############
    # Constants #
    #############

    # 3x3x3
    width = 3

    # Colors
    w = 0; y = 6
    r = 1; o = 5
    b = 2; g = 4

    # Faces
    U = 1; D = 2
    L = 4; R = 8
    F = 16; B = 32

    # Directions
    CW = 1; CCW = -1

    # Axis
    X = 1; Y = 2; Z = 4

    # Type of instructions
    INST_SWAP = 0; INST_ROT = 1


    ####################
    # Internal methods #
    ####################

    def __init__(self):
        """
        Orientation:
            - up: white     bottom: yello
            - front: red    back: orage
        """
        self.faces = {
            self.U: [self.w]*(self.width**2),
            self.D: [self.y]*(self.width**2),
            self.L: [self.g]*(self.width**2),
            self.R: [self.b]*(self.width**2),
            self.F: [self.r]*(self.width**2),
            self.B: [self.o]*(self.width**2)
        }

    def _parse_color(self, color: chr):
        return getattr(self, color)

    def _parse_face(self, face: chr):
        return getattr(self, face)

    def _parse_direction(self, direction: chr):
        if direction == '+':
            return self.CW
        elif direction == '-':
            return self.CCW
        else:
            return None

    def _attr_to_string_by_value(self, attribute_names, value):
        for name in attribute_names:
            if value == getattr(self, name):
                return name

    def _color_to_string(self, color: int):
        return self._attr_to_string_by_value(['w', 'y', 'r', 'o', 'b', 'g'], color)

    def _face_to_string(self, face: int):
        return self._attr_to_string_by_value(['U', 'D', 'L', 'R', 'F', 'B'], face)

    def _direction_to_string(self, direction: int):
        return self._attr_to_string_by_value(['CW', 'CCW'], direction)

    def _axis_to_string(self, axis: int):
        return self._attr_to_string_by_value(['X', 'Y', 'Z'], axis)

    def _get_path_to_dest_face(self, destination: int):
        """
        Get list of instructions of how we can bring the destination face at front.
        """
        to_go = []

        if destination == self.U:
            to_go.append((self.Y, self.CW))
        elif destination == self.D:
            to_go.append((self.Y, self.CCW))
        elif destination == self.L:
            to_go.append((self.Z, self.CCW))
        elif destination == self.R:
            to_go.append((self.Z, self.CW))
        elif destination == self.B:
            to_go.append((self.Z, self.CW))
            to_go.append((self.Z, self.CW))

        to_return = list(map(lambda pair: (pair[0], pair[1] * -1), to_go))
        to_return.reverse()

        return (to_go, to_return)

    def _get_instructions(self, path: list):
        """
        Type of instructions:
            - swap: (INST_SWAP, face_a, face_b)
            - rotate: (INST_ROT, face, direction)

        These are about moving view, not rotating a face!
        """
        instructions = []

        SWAP = lambda a, b: instructions.append((self.INST_SWAP, a, b))
        ROT = lambda a, b: instructions.append((self.INST_ROT, a, b))

        for step in path:
            axis = step[0]
            direction = step[1]

            if axis == self.X:
                if direction > 0:
                    # CW
                    SWAP(self.U, self.R)
                    SWAP(self.U, self.R)
                    SWAP(self.U, self.D)

                    ROT(self.F, self.CW)
                    ROT(self.B, self.CCW)
                else:
                    # CCW
                    SWAP(self.U, self.L)
                    SWAP(self.D, self.R)
                    SWAP(self.U, self.D)

                    ROT(self.F, self.CCW)
                    ROT(self.B, self.CW)

            if axis == self.Y:
                if direction > 0:
                    # CW
                    SWAP(self.U, self.F)
                    SWAP(self.D, self.B)
                    SWAP(self.U, self.D)

                    ROT(self.L, self.CW)
                    ROT(self.R, self.CCW)

                    # Compensate indexing orientation.
                    ROT(self.D, self.CW)
                    ROT(self.D, self.CW)
                    ROT(self.U, self.CW)
                    ROT(self.U, self.CW)
                else:
                    # CCW
                    SWAP(self.U, self.B)
                    SWAP(self.D, self.F)
                    SWAP(self.U, self.D)

                    ROT(self.L, self.CCW)
                    ROT(self.R, self.CW)

                    # Compensate indexing orientation.
                    ROT(self.F, self.CW)
                    ROT(self.F, self.CW)
                    ROT(self.B, self.CW)
                    ROT(self.B, self.CW)

            if axis == self.Z:
                if direction > 0:
                    # CW
                    SWAP(self.B, self.R)
                    SWAP(self.F, self.L)
                    SWAP(self.B, self.F)

                    ROT(self.U, self.CW)
                    ROT(self.D, self.CCW)

                    # Compensate indexing orientation.
                    ROT(self.L, self.CW)
                    ROT(self.R, self.CCW)
                    ROT(self.F, self.CW)
                    ROT(self.B, self.CCW)
                else:
                    # CCW
                    SWAP(self.B, self.L)
                    SWAP(self.F, self.R)
                    SWAP(self.B, self.F)

                    ROT(self.U, self.CCW)
                    ROT(self.D, self.CW)

                    # Compensate indexing orientation.
                    ROT(self.L, self.CW)
                    ROT(self.R, self.CCW)
                    ROT(self.F, self.CCW)
                    ROT(self.B, self.CW)

        return instructions

    def _swap_face(self, a: int, b: int):
        self.faces[a], self.faces[b] = self.faces[b], self.faces[a]

    def _rotate_face(self, face: int, direction: int):
        self.faces[face] = self._square_rotated(self.faces[face], self.width, direction)

    def _swap_part_of_face(self, a: int, a_range: tuple, b: int, b_range: tuple):
        self.faces[a][a_range[0]:a_range[1]+1], self.faces[b][b_range[0]:b_range[1]+1] = self.faces[b][b_range[0]:b_range[1]+1], self.faces[a][a_range[0]:a_range[1]+1]

    def _move_view(self, path: list):
        """
        Rotate view (not the face!) so that the destination face be at front.
        """
        instructions = self._get_instructions(path)

        for step in instructions:
            if step[0] == self.INST_SWAP:
                face_a = step[1]
                face_b = step[2]
                self._swap_face(face_a, face_b)
            elif step[0] == self.INST_ROT:
                face = step[1]
                direction = step[2]
                self._rotate_face(face, direction)

    def _transform_instruction(self, face: int, path: list):
        """
        Transform an instruction along with the path.
        """

        new_face = face
        swaps = self._get_swap_instructions(face, path)

        for step in swaps:
            if new_face == step[0]:
                new_face = step[1]

        return new_face

    def _square_rotated(self, matrix: list, width: int, direction: int, repeat=1):
        if repeat <= 0:
            return matrix

        result = [x for x in matrix]

        if direction == self.CW:
            for i in range(width):
                for j in range(width):
                    result[(i)*width + (j)] = matrix[(width-1-j)*width + (i)]
        elif direction == self.CCW:
            for i in range(width):
                for j in range(width):
                    result[(i)*width + (j)] = matrix[(j)*width + (width-1-i)]

        return self._square_rotated(result, self.width, direction, repeat-1)


    ##################
    # Public methods #
    ##################

    def rotate_face(self, face: chr, direction: chr, verbose=False):
        """
        Rotate the given face of the cube with given direction.
        """
        face = self._parse_face(face)
        if face is None: return

        direction = self._parse_direction(direction)
        if direction is None: return

        # Move the view so the face is at front.
        way_to_go, way_to_return = self._get_path_to_dest_face(face)

        if verbose:
            face_string = self._face_to_string(face)
            direction_string = self._direction_to_string(direction)

            print("We need to bring {face} to front to rotate it {direction}.".format(face=face_string, direction=direction_string))
            print("\nBefore view move:")
            self.dump_figure()

            print("\nPath we need to go: ")
            [print("- {axis} axis {direction} direction".format(axis=self._axis_to_string(step[0]), direction=self._direction_to_string(step[1]))) for step in way_to_go]

            print("\nWay back home: ")
            [print("- {axis} axis {direction} direction".format(axis=self._axis_to_string(step[0]), direction=self._direction_to_string(step[1]))) for step in way_to_go]

        self._move_view(way_to_go)

        if verbose:
            print("\nAfter view move:")
            self.dump_figure()

        # Now the face is at front.

        # Not only the front face, 6~8 blocks of [U, D, L, R] faces are affected.
        affected = (self.width**2 - self.width, self.width**2 - 1)
        swap_part = lambda a, b: self._swap_part_of_face(a, affected, b, affected)

        if direction > 0:
            # CW
            self._rotate_face(self.F, self.CW)
            swap_part(self.U, self.R)
            swap_part(self.D, self.L)
        else:
            # CCW
            self._rotate_face(self.F, self.CCW)
            swap_part(self.U, self.L)
            swap_part(self.D, self.R)

        swap_part(self.U, self.D)

        if verbose:
            print("\nAfter rotate:")
            self.dump_figure()

        self._move_view(way_to_return)

        if verbose:
            print("\nAfter view restore:")
            self.dump_figure()
            print("\n")

    def dump(self, face: int):
        """
        Print a single side of the cube.
        """
        for i in range(self.width):
            for j in range(self.width):
                print(self._color_to_string(self.faces[face][i*self.width + j]), end='')
            print("")

    def dump_figure(self, padding=1, border=True):
        if border:
            print("{space} Dump started {space}".format(space='='*(self.width*2)))

        rotated = lambda m, d, r: self._square_rotated(matrix=self.faces[m], width=self.width, direction=d, repeat=r)
        print_color = lambda m, i, j: print("{color}".format(color=self._color_to_string(m[i*self.width + j])), end='')

        up = rotated(self.U, 0, 0)
        left = rotated(self.L, self.CCW, 1)
        front = rotated(self.F, 0, 0)
        back = rotated(self.B, 0, 0)
        right = rotated(self.R, self.CW, 1)
        down = rotated(self.D, self.CW, 2)

        # Up
        for i in range(self.width):
            print(' '*(self.width+padding), end='')
            for j in range(self.width):
                print_color(up, i, j)
            print('')

        print('\n'*padding, end='')

        # Left, front, right, back
        mid_faces = [left, front, right, back]
        for i in range(self.width):
            for j in range(len(mid_faces)):
                for k in range(self.width):
                    print_color(mid_faces[j], i, k)
                print(' '*padding, end='')
            print('')

        print('\n'*padding, end='')

        # Down
        for i in range(self.width):
            print(' '*(self.width+padding), end='')
            for j in range(self.width):
                print_color(down, i, j)
            print('')

        if border:
            print("{space} Dump finished {space}".format(space='='*(self.width*2)))


def get_cases():
    n_cases = int(input())
    cases = []

    for _ in range(n_cases):
        n_instructions = int(input())
        instructions = []
        for instruction in input().split():
            instructions.append((instruction[0:1], instruction[1:2]))
        cases.append(instructions)

    return cases


def from_input():
    for case in get_cases():
        cube = Cube()
        for instruction in case:
            cube.rotate_face(instruction[0], instruction[1])
        cube.dump(Cube.U)


from_input()
