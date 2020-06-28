""" serializer_demo.py
    An application that needs to convert a Song object into its string
    representation using a specified format.
    Inspired from https://realpython.com/factory-method-python/
    Single-responsibility Principle (SRP) https://en.wikipedia.org/wiki/Single-responsibility_principle
    Code refactoring: https://en.wikipedia.org/wiki/Code_refactoring
"""

import json
import xml.etree.ElementTree as et

class Song:
    """ Class that contains the basic info on a song
        song_id: unique number
        title: name of the song
        artist: name of the artist
    """
    def __init__(self, song_id: int, title: str, artist: str) -> None:
        """ Initialize. Missing error checking for unique song_id.
        """
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    """ Class that can convert a song object into its string representation
        according to the value of the format parameter.
    """
    def serialize(self, song, format: str):
        """ upports two different formats: JSON and XML.
            Any other format specified is not supported, so a ValueError exception is raised
        """
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(song_info)
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        else:
            raise ValueError(format)

class SongSerializer_new:
    """ Class that can convert a song object into its string representation
        according to the value of the format parameter. Implemented SRP.
    """
    def serialize(self, song, format: str):
        """ Invoke the right serializing function based on format. """
        if format == 'JSON':
            return self._serialize_to_json(song)
        elif format == 'XML':
            return self._serialize_to_xml(song)
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        """ Single purpose function. """
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        """ Single purpose function. """
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')

class SongSerializer_Factory_Method:
    """ Class that can convert a song object into its string representation
        according to the value of the format parameter.
        The central idea in Factory Method is to provide a separate component with the
        responsibility to decide which concrete implementation should be used based on
        some specified parameter. That parameter in our example is the format.

        To complete the implementation of Factory Method, you add a new method
        ._get_serializer() that takes the desired format. This method evaluates
        the value of format and returns the matching serialization function
    """
    def serialize(self, song, format: str):
        """ Call the right serializer. Depends on an interface to complete its task.
            It is the client component of the pattern.
        """
        serializer = get_serializer(format)
        return serializer(song)

    def get_serializer(format: str):
        """ Returns the matching serialization function based on format.
            Creator component. The creator decides which concrete implementation to use.
        """
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        """ Product is a function that takes a Song and returns a string representation. """
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        """ Product is a function that takes a Song and returns a string representation. """
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')

# Initialize a song using the Song() Class
song = Song('1', 'Water of Love', 'Dire Straits')

# Initialize a SonSerializer() Class
serializer = SongSerializer()

# Use it
print(serializer.serialize(song, 'JSON'))
print(serializer.serialize(song, 'XML'))
#print(serializer.serialize(song, 'YAML'))

serializer = SongSerializer_new()
print(serializer.serialize(song, 'JSON'))
print(serializer.serialize(song, 'XML'))

serializer = SongSerializer_Factory_Method()
print(serializer.serialize(song, 'JSON'))
print(serializer.serialize(song, 'XML'))