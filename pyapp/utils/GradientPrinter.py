class GradientPrinter:
    """
    A class for printing text with a gradient of colors.
    """

    @staticmethod
    def interpolate(start, end, factor):
        """
        Perform linear interpolation between two values.
        """
        return int(start + (end - start) * factor)

    @staticmethod
    def gradient_text(text, start_color, end_color):
        """
        Print a gradient of text from start_color to end_color.
        - text: The text to print
        - start_color, end_color: RGB tuples for the start and end colors
        """
        gradient = []
        length = len(text)
        for i, char in enumerate(text):
            factor = i / (length - 1) if length > 1 else 0
            r = GradientPrinter.interpolate(start_color[0], end_color[0], factor)
            g = GradientPrinter.interpolate(start_color[1], end_color[1], factor)
            b = GradientPrinter.interpolate(start_color[2], end_color[2], factor)
            gradient.append(f"\033[38;2;{r};{g};{b}m{char}")

        print("".join(gradient) + "\033[0m")
