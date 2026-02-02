class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
    	raise NotImplementedError
    	
    def props_to_html(self):
    	if self.props == None:
    	    return ""
    	props_html = ""
    	for prop in self.props:
    	    props_html += f' {prop}="{self.props[prop]}"'
    	return props_html
    	
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("This is a ValueError for a missing value!")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
class ParentNode(HTMLNode):
    def __init__(self, tag , children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
    	if self.tag == None:
    	    raise ValueError("This is a ValueError for a missing tag!")
    	if self.children == None:
    	    raise ValueError("This is a ValueError for missing children!")
    	children_html = ""
    	for child in self.children:
    	    children_html += child.to_html()
    	return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        
    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)

        if text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)

        if text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)

        if text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)

        if text_node.text_type == TextType.LINK:
            if text_node.url is None:
                raise ValueError("LINK TextNode must have a url")
            return LeafNode(
                "a",
                text_node.text,
                props={"href": text_node.url}
            )

        if text_node.text_type == TextType.IMAGE:
            if text_node.url is None:
                raise ValueError("IMAGE TextNode must have a url")
            return LeafNode(
                "img",
                "",
                props={
                    "src": text_node.url,
                    "alt": text_node.text
                }
            )

        raise Exception(f"Unsupported TextType: {text_node.text_type}")
        
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []

        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue

            parts = node.text.split(delimiter)

            if len(parts) % 2 == 0:
                raise ValueError(f"Invalid markdown: unclosed delimiter {delimiter}")

            for i, part in enumerate(parts):
                if part == "":
                    continue

                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))

        return new_nodes







