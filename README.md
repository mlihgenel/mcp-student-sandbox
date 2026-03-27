# Mystery Module

## Overview

Mystery Module is a lightweight Python module designed to solve quadratic equations of the form \(ax^2 + bx + c = 0\). It provides a simple and efficient function to compute the roots of such equations, handling both real and complex cases.

## Features

- Computes real roots for quadratic equations
- Returns `None` for equations with complex roots
- Minimal dependencies (only uses Python's built-in `math` module)
- Easy to integrate into larger projects

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone or download the repository containing `mystery_module.py`.
3. Place the file in your project directory or Python path.

No additional installation steps are required as the module uses only standard library components.

## Usage

Import the module and call the `fn_x` function with the coefficients `a`, `b`, and `c`.

### Example

```python
import mystery_module

# Solve x² - 3x + 2 = 0
roots = mystery_module.fn_x(1, -3, 2)
print(roots)  # Output: (2.0, 1.0)

# Solve x² + 2x + 5 = 0 (complex roots)
roots = mystery_module.fn_x(1, 2, 5)
print(roots)  # Output: None
```

## API Reference

### `fn_x(a, b, c)`

Computes the roots of the quadratic equation \(ax^2 + bx + c = 0\).

#### Parameters
- `a` (float): Coefficient of \(x^2\)
- `b` (float): Coefficient of \(x\)
- `c` (float): Constant term

#### Returns
- `tuple` of two floats: The real roots of the equation (may be identical if discriminant is zero)
- `None`: If the discriminant is negative (complex roots)

#### Notes
- The function uses the quadratic formula: \(x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\)
- For complex roots, the function returns `None` instead of complex numbers

## Mathematical Background

The quadratic formula is derived from completing the square or using the discriminant \(d = b^2 - 4ac\):

- If \(d > 0\): Two distinct real roots
- If \(d = 0\): One real root (repeated)
- If \(d < 0\): Two complex roots

This module focuses on real roots only.

## Contributing

Contributions are welcome! Please ensure that any changes maintain the module's simplicity and efficiency.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or feedback, please open an issue in the repository.