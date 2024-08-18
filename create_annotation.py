import xml.etree.ElementTree as ET


def create_annotations_xml(blocklist_file: str, annotations_file: str) -> None:
    """Creates an annotations.xml file from a text file of blocklisted domains.


    Args:
        blocklist_file: Path to the blocklist file.
        annotations_file: Path to the annotations.xml file.
    """
    root = ET.Element("Annotations", xmlns="http://www.google.com/cse/api/0.1")

    with open(blocklist_file, "r") as fp:
        domains = fp.read().splitlines()

    for domain in domains:
        domain = domain.strip()
        annotation = ET.SubElement(root, "Annotation")
        annotation.set("about", "*.{}/*".format(domain))
        annotation.set(
            "timestamp", "0x0006112774077369"
        )  # Timestamp is hardcoded, I'm assuming this is UNIX timestamp in milliseconds
        annotation.set("score", "1.0")

        label = ET.SubElement(annotation, "Label")
        label.set("name", "_exclude_")

        additional_data = ET.SubElement(annotation, "AdditionalData")
        additional_data.set("attribute", "original_url")
        additional_data.text = "*.{}/*".format(domain)

    tree = ET.ElementTree(root)
    tree.write(
        annotations_file,
        encoding="utf-8",
        xml_declaration=True,
        short_empty_elements=False,
    )


if __name__ == "__main__":
    blocklist_file = "path/to/blocklist.txt"
    annotations_file = "path/to/annotations.xml"
    create_annotations_xml(blocklist_file, annotations_file)
