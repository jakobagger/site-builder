import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        dict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=dict)
        expected_output = f' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_with_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_len_zero(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")
