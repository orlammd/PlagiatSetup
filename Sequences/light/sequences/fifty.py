import sys
sys.path.append("../Controls/Mididings/")

from ports import *

fifty_offre_emploi=[
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Rémunération : >NON<\n URGENT\n contact: fiducials@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Pas de ça entre nous, on est avant tout une équipe\n URGENT\n contact: financier@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n coCOFFEE needed\n URGENT\n contact: coco@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n CCoffee NEEDED\n URGENT\n contact: ccoffee@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche tondeur débroussailleur sexy raffiné\n URGENT\n contact: epilation@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche tondeuse débroussailleuse Briggs et Stratton\n URGENT\n contact: deb@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Aimerait : retour de l'être aimé, départ de l'être pas aimé\n URGENT\n contact: grandgourou@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Trouverait plan de carrière 100% réussite\n URGENT\n contact: medium@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Rémunération : >NON<\n URGENT\n contact: fiducials@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Pas de ça entre nous, on est avant tout une équipe\n URGENT\n contact: financier@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n coCOFFEE needed\n URGENT\n contact: coco@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n CCoffee NEEDED\n URGENT\n contact: ccoffee@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Rémunération : >NON<\n URGENT\n contact: fiducials@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Pas de ça entre nous, on est avant tout une équipe\n URGENT\n contact: financier@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n coCOFFEE needed\n URGENT\n contact: coco@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n CCoffee NEEDED\n URGENT\n contact: ccoffee@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],

]
