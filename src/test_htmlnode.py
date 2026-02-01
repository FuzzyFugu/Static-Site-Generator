import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "This is a text", "child", {"href": "https://google.com", "target": "_blank"})
        node2 = HTMLNode("a", "This is a text", "child", {"href": "https://google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("p", "This is a text", "child", {"href": "https://google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is not a text", "child", {"href": "https://google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = HTMLNode("p", "This is a text", "child", {"href": "https://google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is a text", "child", {"href": "https://gogu.com", "target": "_blank"})
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
