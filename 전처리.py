# -*- coding: utf-8 -*-
"""전처리.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j9VZkFSXjyhjk121N_tfNDd2azMImFre
"""

!pip install kss
!pip install konlpy
!pip install git+https://github.com/ssut/py-hanspell.git
!pip install git+https://github.com/haven-jeon/PyKoSpacing.git

#정제되지 않은 텍스트 예시
text='저는 enfp유형인데 저 같은 성향을 가진 사람들은 어떻게 행동하는지 궁금해서 글남겨요!저는 힘든상황이 있을때 가족들한테 털어놓고 어떻게든 그 상황을 해결해나가려고 하는 편이에요.친구들한테도 힘든상황에 대해서 감정적으로 울고불며 그렇게 잘 털어놓지 않고 전혀 티내지도 않아요.항상 긍정적인 모습을 주로 보여주긴해요.어차피 내가 해결해야할 일이고, 나로인해 상대가 걱정하는것도 싫고 제 우울한 감정을 친구한테 전달하고 싶지 않아서 그런거 같아요. 그래도 정말 친한 친구들이랑은 만날때 어느정도 문제가 해결되어갈때 쯤 이런상황이 있었고 힘들었다. 이렇게 털어놓는 편이에요. 근데 어느날 한 지인(이성)이  저한테 너는 힘들면 힘들다고 말하는걸 못봐서 털어놨으면 좋겠는데 라고 말하길래다른 사람들은 그럼 힘들때 어떻게 하는지 궁금해지더라구요.제가 좀 제 감정표현을 하는데 서툰게 없지않아 있긴하지만 남한테 그렇게 힘들때 다들 털어놓으시나요어떻게 지인들에게 감정적인 표현을 다들하시는지 궁금해요.'

#pykospacing 패키지

from pykospacing import Spacing
spacing = Spacing()
kospacing_sent = spacing(text) 
print(kospacing_sent)

#py-hanspell 패키지
from hanspell import spell_checker
spelled_sent = spell_checker.check(text)
hanspell_sent = spelled_sent.checked
print(hanspell_sent)

#kss - 문장 토큰화
import kss
kss_complete_text = kss.split_sentences(hanspell_sent)
print(kss_complete_text)

#형태소 토큰화
import konlpy
from konlpy.tag import Okt  
okt=Okt()
size = len(kss_complete_text)
for i in range(size):
  print(okt.morphs(kss_complete_text[i]))