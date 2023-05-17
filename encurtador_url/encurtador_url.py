class EncurtadorURL: # URLShortener
    def __init__(self, url):
        self.url = url
        self.shortened_url = None

    def display_shortened_url(self):
        print(f"Original URL: {self.url}")
        print(f"Shortened URL: {self.shortened_url}")
