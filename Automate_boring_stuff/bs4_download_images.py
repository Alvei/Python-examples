""" Download jpg/png images from Imgur that match a user's search term(s).
    from github: IFinners/automate-the-boring-stuff-projects"""

import os
import requests
import bs4

def image_downloader(search: str, extension: str, save=False) -> int:
    """ Search for and download all images of the argument type from Imgur."""
    #url = 'http://imgur.com/search?q=' + search + ' ext:' + extension
    url = 'http://imgur.com/search?q_all=' + search + '&q_type=' + extension
    image_dir = 'imgur'
    os.makedirs(image_dir, exist_ok=True)  # Store comics in ./xkcd
    max_image = 10

    print(f"Opening url:{url}")
    res = requests.get(url)
    res.raise_for_status()

    # Convert the page into bs4 object
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # The code inside the select is unclear
    image_elem = soup.select('.post > .image-list-link img')
    print(f"Found {len(image_elem)} images")

    for index, image in enumerate(image_elem):
        if index < max_image: # Download only a certain number of images

            # Convert image URL from thumbnail size to fullsize version
            image_url_s = 'https:' + image_elem[index].get('src')
            image_url = image_url_s[: -5] + '.' + extension

            print(f'Downloading image {index}: {image_url}')
            res = requests.get(image_url)
            res.raise_for_status()

            # if the save flag is true save the images
            if save:
                image_file = open(os.path.join(image_dir,
                                                os.path.basename(image_url)), 'wb')
                for chunk in res.iter_content(1000000):
                    image_file.write(chunk)
                image_file.close()

    return min(len(image_elem), max_image)

def main():
    """ Main program. Define the search words and the file extensions."""

    #search = input('Enter desired search term(s): ')
    search = 'robot'
    extensions = ['jpg', 'png']
    downloaded = 0
    for ext in extensions:
        downloaded += image_downloader(search, ext, True)

    if downloaded == 0:
        print('No images found.')
    else:
        print(f'All {downloaded} files successfully downloaded.')

if __name__ == "__main__":
    main()
