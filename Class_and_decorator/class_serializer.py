""" serializer_demo.py
    An application that needs to convert a Song object into its string
    representation using a specified format. Done with 3 different implementations
    Inspired from
          https://realpython.com/factory-method-python/
    Single-responsibility Principle (SRP)
          https://en.wikipedia.org/wiki/Single-responsibility_principle
    Code refactoring:
          https://en.wikipedia.org/wiki/Code_refactoring
    xml:
    https://docs.python.org/2/library/xml.etree.elementtree.html

    ElementTree(element=None, file=None) wrapper class that represents an entire
    element hierarchy, & adds some extra support for serialization to & from XML.
    element is the root element for this tree.
"""

import json
import xml.etree.ElementTree as et


class Song:
    """ Class that contains the basic info on a song. """

    def __init__(self, song_id: int, title: str, artist: str) -> None:
        """Initialize. Missing error checking for unique song_id."""
        self.song_id = song_id  # Unique number
        self.title = title  # Song name
        self.artist = artist  # Artist name

    def __repr__(self):
        """ printing. """
        return f"ID: {self.song_id}, title: {self.title}, artist: {self.artist}"

    def __str__(self):
        """ printing. """
        return f"ID: {self.song_id}, title: {self.title}, artist: {self.artist}"


class SongSerializer:
    """ Converts a song object into its string representation
        according to the value of the format parameter."""

    def serialize(self, song: Song, song_format: str) -> str:
        """ Supports 2 different formats: JSON and XML.
            Other format not supported, ValueError exception is raised."""
        if song_format == "JSON":
            song_info = {"id": song.song_id, "title": song.title, "artist": song.artist}
            return json.dumps(song_info)
        if song_format == "XML":
            # Element(tag, attrib={}, **extra)
            # tag is the element name. attrib is an optional dictionary, containing element attributes
            song_info = et.Element("song", attrib={"id": song.song_id})
            title = et.SubElement(song_info, "title")
            title.text = song.title
            artist = et.SubElement(song_info, "artist")
            artist.text = song.artist
            return et.tostring(song_info, encoding="unicode")
        raise ValueError(song_format)


class SongSerializerNew:
    """ Converts a song object into its string representation
        according to the value of the format parameter.
        Implemented SRP. """

    def serialize(self, song: Song, song_format: str) -> str:
        """ Invoke the right serializing function based on format. """
        if song_format == "JSON":
            return self._serialize_to_json(song)
        if song_format == "XML":
            return self._serialize_to_xml(song)
        raise ValueError(song_format)  # Default

    def _serialize_to_json(self, song):
        """ Single purpose function. """
        payload = {"id": song.song_id, "title": song.title, "artist": song.artist}
        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        """ Single purpose function. """
        song_element = et.Element("song", attrib={"id": song.song_id})
        title = et.SubElement(song_element, "title")
        title.text = song.title
        artist = et.SubElement(song_element, "artist")
        artist.text = song.artist
        return et.tostring(song_element, encoding="unicode")


def get_serializer(song_format: str):
    """ Returns the matching serialization function based on format.
        Creator component. The creator decides which concrete
        implementation to use.
    """
    if song_format == "JSON":
        return _serialize_to_json
    if song_format == "XML":
        return _serialize_to_xml
    raise ValueError(song_format)  # Default


def _serialize_to_json(song):
    """ Product is a function that takes a Song and returns a string representation. """
    payload = {"id": song.song_id, "title": song.title, "artist": song.artist}
    return json.dumps(payload)


def _serialize_to_xml(song):
    """ Product is a function that takes a Song and returns a string representation. """
    song_element = et.Element("song", attrib={"id": song.song_id})
    title = et.SubElement(song_element, "title")
    title.text = song.title
    artist = et.SubElement(song_element, "artist")
    artist.text = song.artist
    return et.tostring(song_element, encoding="unicode")


class SongSerializerFactoryMethod:
    """ Clonverts a song object into its string representation
        according to the value of the format parameter.

    The central idea in Factory Method is to provide a separate component with the
    responsibility to decide which concrete implementation should be used based on
    some specified parameter. That parameter in our example is the format.

    To complete the implementation of Factory Method, you add a new method
    ._get_serializer() that takes the desired format. This method evaluates
    the value of format and returns the matching serialization function.

    Note that it does not use as many methods but functions.
    """

    def serialize(self, song, song_format: str):
        """Call the right serializer. Depends on an interface to complete its task.
        It is the client component of the pattern.
        """
        serializer = get_serializer(song_format)
        return serializer(song)


def main():
    """ test harness. """
    # Initialize a song using the Song() Class and then the SongSerializer() Class
    song = Song("1", "Water of Love", "Dire Straits")
    serializer = SongSerializer()
    print(song)

    # Use it
    print("\nFirst implementation:")
    print(serializer.serialize(song, "JSON"))
    print(serializer.serialize(song, "XML"))
    # print(serializer.serialize(song, 'YAML'))

    ###########################################
    serializer = SongSerializerNew()
    print("\nSecond implementation:")
    print(serializer.serialize(song, "JSON"))
    print(serializer.serialize(song, "XML"))

    ###########################################
    serializer = SongSerializerFactoryMethod()
    print("\nThird implementation:")
    print(serializer.serialize(song, "JSON"))
    print(serializer.serialize(song, "XML"))


if __name__ == "__main__":
    main()
