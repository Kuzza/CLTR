import unittest
from text_handlers import TextClassifier

class TestTextClassifier(unittest.TestCase):

    def setUp(self):
        # The languages configurations are redefined (even they are the same 
        # of the default configurations) because they can be changed by the user, 
        # and the test may not work only because of it.
        
        self.config = {
            "english" : ["and", "the", "yes", "if", "then", "ever",
                         "never", "all", "nothing", "for", "do", "of", "to"],
            "italian" : ["e", "il", "lo", "la", "i", "gli", "se", "da",
                         "fra", "si", "no", "quindi", "tutto", "niente",
                         "sepmpre", "mai", "per", "fare", "di", "a"],
            "french" : ["et", "aux", "les", "oui", "puis", "partout", 
                        "toujours", "jamais", "rien", "pour", "faire", "de"]
           }
        
        self.text_classifier = TextClassifier(self.config)  
        self.text_samples = {
        "english": ["God Save our gracious Queen! "\
                    "Long live our noble Queen, God save the Queen!"\
                    "Send her victorious, happy and glorious, "\
                    "long to reign over us, God save the Queen!",
                    
                    "O Lord, our God, arise,"\
                    "scatter her enemies, "\
                    "and make them fall."\
                    "Confound their politics,"\
                    "frustrate their knavish tricks,"\
                    "on thee our hopes we fix,"\
                    "God save us all.",
                    
                    "Thy choicest gifts in store"\
                    "on her be pleased to pour,"\
                    "long may she reign!"\
                    "May she defend our laws, "\
                    "and ever give us cause"\
                    "to sing with heart and voice,"\
                    "God save the Queen!"                    
                    ],
        
        "italian": ["Fratelli d'Italia,"\
                    "l'Italia s'è desta, "\
                    "dell'elmo di Scipio"\
                    "s'è cinta la testa."\
                    "Dov'è la Vittoria?"\
                    "Le porga la chioma,"\
                    "che schiava di Roma"\
                    "Iddio la creò.",
                    
                    "Stringiamoci a coorte,"\
                    "siam pronti alla morte."\
                    "Siam pronti alla morte,"\
                    "l'Italia chiamò."\
                    "Stringiamoci a coorte,"\
                    "siam pronti alla morte."\
                    "Siam pronti alla morte,"\
                    "l'Italia chiamò, sì!",
                    
                    "Noi fummo da secoli"\
                    "calpesti, derisi,"\
                    "perché non siam popoli,"\
                    "perché siam divisi."\
                    "Raccolgaci un'unica"\
                    "bandiera, una speme:"\
                    "di fonderci insieme"\
                    "già l'ora suonò."
                    ],
        
        "german": ["Deutschland, Deutschland über alles,"\
                   "über alles in der Welt,"\
                   "wenn es stets zum Schutz und Trutze"\
                   "brüderlich zusammenhält."\
                   "Von der Maas bis an die Memel,"\
                   "von der Etsch bis an den Belt:"\
                   "Deutschland, Deutschland über alles,"\
                   "über alles in der Welt.",
                   
                   "Deutsche Frauen, deutsche Treue,"\
                   "deutscher Wein und deutscher Sang"\
                   "sollen in der Welt behalten"\
                   "ihren alten schönen Klang."\
                   "Uns zu edler Tat begeistern"\
                   "unser ganzes Leben lang"\
                   "Deutsche Frauen, deutsche Treue,"\
                   "deutscher Wein und deutscher Sang.",
                   
                   "Einigkeit und Recht und Freiheit"\
                   "für das deutsche Vaterland!"\
                   "Danach lasst uns alle streben,"\
                   "brüderlich mit Herz und Hand!"\
                   "Einigkeit und Recht und Freiheit"\
                   "sind des Glückes Unterpfand."\
                   "Blüh im Glanze dieses Glückes,"\
                   "blühe deutsches Vaterland."
                   ],
        
        "french": ["Allons enfants de la Patrie,"\
                   "Le jour de gloire est arrivé!"\
                   "Contre nous de la tyrannie,"\
                   "L’étendard sanglant est levé!"\
                   "L’étendard sanglant est levé!"\
                   "Entendez-vous dans les campagnes"\
                   "Mugir ces féroces soldats?"\
                   "Ils viennent jusque dans nos bras"\
                   "Egorger nos fils et nos compagnes!",
                   
                   "Aux armes, citoyens!"\
                   "Formez vos bataillons!"\
                   "Marchons! Marchons!"\
                   "Qu’un sang impur"\
                   "Abreuve nos sillons!",
                   
                   "Que veut cette horde d’esclaves,"\
                   "De traîtres, de rois conjurés?"\
                   "Pour qui ces ignobles entraves,"\
                   "Ces fers dès longtemps préparés?"\
                   "Ces fers dès longtemps préparés?"\
                   "Français, pour nous, ah! Quel outrage!"\
                   "Quels transports il doit exciter!"\
                   "C’est nous qu’on ose méditer"\
                   "De rendre à l’antique esclavage!"]        
        }

    def test_classify(self):
        for language, text_list in self.text_samples.items():
            for text in text_list:
                res_language = self.text_classifier.DetectLanguage3(text)
                if language in self.config:
                    self.assertEqual(language, res_language)
                else:
                    self.assertEqual(self.text_classifier.GetUnknownMsg(), res_language)


if __name__ == '__main__':
    unittest.main()