class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created +=1

    @classmethod
    def get_number_of_watches_created(cls):
        return 'The current number is: {}'.format(cls.watches_created)

    @classmethod
    def including_engraving(cls, text):
            if LuxuryWatch.validate(text):
                print('We can use', text, 'to make it')
                new_feature = cls()
                new_feature.engraving = text
                print('You ordered the watch with engraving {}'.format(new_feature.engraving))
                return new_feature
            else:
                print('The text', text, 'is invalid')

    @staticmethod
    def validate(text):
        if len(text) <= 40 and text.isalnum():
            return True
        else:
            return False

print(LuxuryWatch.get_number_of_watches_created())
watch_1=LuxuryWatch()
print(LuxuryWatch.get_number_of_watches_created())
watch2=LuxuryWatch.including_engraving('22101992')
print(LuxuryWatch.get_number_of_watches_created())
watch3=LuxuryWatch.including_engraving('foo@baz.com')
print(LuxuryWatch.get_number_of_watches_created())


