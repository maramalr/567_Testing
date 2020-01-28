import unittest

def classify_triangle(x,y,z):
    """ function to classify type of triangles where x, y and z are the lengths of sides """

    if x > 0 and y > 0 and z > 0 : #if any of length is zero then false

        if x == y and x == z and y==z :
            return 'equilateral'
        
        elif x == y and x != z and y != z :
            return 'isoscels'
        
        elif x != y and x != z and y != z and (x*x) + (y*y) != (z*z):
            return 'scalene'
        
        elif (x*x) + (y*y) == (z*z) :
            return 'right'

    else:
        return 'false'

def main ():
    'to demonstrate the result'

    print(classify_triangle(3,3,3))
    print(classify_triangle(3,3,2))
    print(classify_triangle(1,2,3))
    print(classify_triangle(6,8,10))
    print(classify_triangle(0,3,3))

main()

class Classify_triangle_Test(unittest.TestCase):

    def test_classify_triangle(self):
        ' test triangles method'

        self.assertEqual(classify_triangle(3,3,3), 'equilateral')
        self.assertEqual(classify_triangle(3,3,2), 'isoscels')
        self.assertNotEqual(classify_triangle(0,3,3), 'isoscels')
        self.assertEqual(classify_triangle(1,2,3), 'scalene')
        self.assertTrue(classify_triangle(0,3,1), 'false')
        self.assertEqual(classify_triangle(6,8,10), 'right')
        self.assertNotEqual(classify_triangle(2,2,10),'right' )

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)