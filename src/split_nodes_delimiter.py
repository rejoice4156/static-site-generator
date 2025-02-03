from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)

        elif old_node.text.count(delimiter) != 2:
            raise Exception('Invalid Markdown syntax')

        else:
            old_node_parts = []
            old_node_text_parts = old_node.text.split(delimiter)
            old_node_parts.append(TextNode(old_node_text_parts[0], TextType.NORMAL))

            if delimiter == '**':
                old_node_parts.append(TextNode(old_node_text_parts[1], TextType.BOLD))
            elif delimiter == '*':
                old_node_parts.append(TextNode(old_node_text_parts[1], TextType.ITALIC))
            elif delimiter == '`':
                old_node_parts.append(TextNode(old_node_text_parts[1], TextType.CODE))

            old_node_parts.append(TextNode(old_node_text_parts[2], TextType.NORMAL))
            new_nodes.extend(old_node_parts)

    return new_nodes
