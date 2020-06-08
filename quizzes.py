class pictureQuiz:
    def __init__(self, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, a5, a6, c1, c2, c3, c4, c5, c6, headline, description):
        self.questions = [q1, q2, q3, q4, q5, q6]
        self.answers = [a1, a2, a3, a4, a5, a6]
        self.credits = [c1, c2, c3, c4, c5, c6]
        self.headline = headline
        self.description = description

beaches = pictureQuiz('https://live.staticflickr.com/2831/9378481418_9486c5f64a_b.jpg', 'https://live.staticflickr.com/2864/9511407504_8877c7b9a4_b.jpg', 'https://farm9.staticflickr.com/8005/6982732686_63618d0e48_b.jpg', 'http://s0.geograph.org.uk/photos/74/27/742730_505bf2dc.jpg', 'https://live.staticflickr.com/65535/49114791961_9cc6054a1b_b.jpg', 'https://live.staticflickr.com/1094/1466156787_eced7cda81_b.jpg', 'rhossili', 'barafundle bay', 'marloes sands', 'mwnt', 'porthdinllaen', 'three cliffs bay', 'Nigel Swales license CC BY-SA 2', 'rhedeg license CC BY 2', 'Carnachenwen Mathry license CC BY-ND 2', 'Bob Jones license CC BY-SA 2', 'ohefin license CC BY-SA 2', 'ladyr6 license CC BY-ND 2', headline='Beaches', description='Can you name these beautiful beaches?')