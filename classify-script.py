#!/usr/bin/python
# -*- coding: utf-8 -*

def clean_string(string):
 	'''
 	Remove uncounted characters from the string.
 	'''
 	return string

def ratio_distinct(text):
	'''Ratio of unique characters to total number of characters in the text.
	
	:param text: any sample string
	:returns: ratio of unique symbols to total symbols in sample
	'''
	ratio = count_distinct(text)/len(text)
	return ratio

def count_distinct(string):
	'''Count the number of unique symbols in this string.

	:param string: any piece of text
	:returns: count of distinct glyphs in string
	'''
	# set codec
	string = string.decode('utf-8')
	# count unique characters in string
	count = (len(set(string)))
	return count

def classify_script(symbols, script='This script', double_bit=False):
	'''Guess the classification of this script by counting the number of distinct characters it contains. Accuracy increases as the number of unique symbols in this sample approaches the total number of signs in the script.

	:param symbols: string containing characters in a single script
	:param script: optional string naming the script
	:param double_bit: optional Boolean to avoid double-counting double-bit characters. ALWAYS SET FALSE if count_distinct decodes utf-8 chars
	:returns: script_type: formatted string guessing the classification of the script
	'''
	num_signs = count_distinct(symbols)

	if num_signs <= 40*(double_bit+1):
		script_type = "%s is alphabetic!"%script
	elif num_signs < 100*(double_bit+1):
		script_type = "%s is syllabic!"%script
	else:
		script_type = "%s is logophonetic!"%script

	return script_type

script_name = raw_input('Script name:')
script_signs = raw_input('Example of the script:')

print (classify_script(script_signs, script_name))

#script_name = 'English'
#script_signs = 'abcdefghijklmnopqrstuvwxyz'
#script_signs = 'I am typing this little piece of text in English. Hopefully it is good enough to give that little function an idea of how this writing system works. It should tell us that it\'s written in an alphabet.'

#script_name = 'Hawaiian'
#script_signs = 'Haʻaheo ka ua i nā pali, ke nihi aʻela i ka nahele, e hahai ana paha i ka liko, pua ʻāhihi lehua o uka. Aloha ʻoe, aloha ʻoe, e ke onaona noho i ka lipo'

#script_name = 'Hiragana'
#script_signs = 'あいうえおかきくけこさしすせそたちつてとはひふへほまみむめもなにぬねのらりるれろわをやゆよ'

#script_name = 'Kanji'
#script_signs = '日一国会人年大十二本中長出三同時政事自行社見月分議後前民生連五発間対上部東者党地合市業内相方四定今回新場金員九入選立開手米力学問高代明実円関決子動京全目表戦経通外最言氏現理調体化田当八六約主題下首意法不来作性的要用制治度務強気小七成期公持野協取都和統以機平総加山思家話世受区領多県続進正安設保改数記院女初北午指権心界支第産結百派点教報済書府活原先共得解名交資予川向際査勝面委告軍文反元重近千考判認画海参売利組知案道信策集在件団別物側任引使求所次水半品昨論計死官増係感特情投示変打男基私各始島直両朝革価式確村提運終挙果西勢減台広容必応演電住争談能無再位置真流格有疑口過局少放税検町常校料裁状工建語球営空職証土急止送供可役構木割聞身費付切由説転食比難防補車優夫研収断何南石足消境神番規術護展態導備宅害配副算視条幹独警宮究育席輸訪楽起万着乗店述残想線率病農州武声質念待試族象銀域助労例衛然早張映限親額験追商葉義伝働形景落担好退準賞辺造英株頭技低毎医復仕去姿味負閣失移差衆個門写評課末守若脳極種美命福蔵量望松非観察整段横型白深字答夜製票音申様財港識注呼達良帰針専推谷古候史天階程満敗管値歌買兵接器士光討路悪科授細効図週積丸他録処省旧室憲太橋歩岸客風紙激否周師材登系批母易健黒火戸速存花春飛殺央券赤号単盟座青破編竹除完降責並従右修隊危採織森競拡故館給屋読弁根色友苦就走園具左異歴辞将秋因厳馬愛休富父遺未貿講林装諸夏素亡劇河航冷模適婦鉄寄益顔類児余禁印逆王返標久短油妻暴輪宣背昭植熱宿薬清習険覚盛船倍均億圧芸許皇臨駅署便留罪停興陸玉源波創障筋帯延羽努固精則乱散司康測豊洋静善厚喜囲卒略承順紀旅絶級幸岩練軽庁博城等救層版老令角損曲裏密庭徒仏績築貨志混池我勤血幕居染温雑招季困星傷永著誌庫刊像功欠秘坂刻底賛服犯布寺息宇遠養街願絵希欲痛縮枚属笑複郵束仲栄札似夕板列探借節骨射届曜遊迷夢巻揮君燃雨閉包弱賃折郡草飲貴災暮預焼簡肉納樹章臓律貸至宗照宙酒銭堂群悲秒操晴誕謝孝仮暗鳥純飯訳吸典賀看勉奏翌陽快片郷敬泉冬徳皮漁里己貯歯忠倉昼茶柱沿唱祭誠忘雪筆訓浴俳童宝胸砂塩誤序弟聖洗舎兆畑慣毛緑尊祝礼窓旗詩昔牛敵魚液貧衣酸兄泳祖幼荷潮梅桜黄句鋼臣浅雲縦捨鳴腹乳矢紅炭丁冊勇械犬菜耳仁墓卵湖干頂虫刷湯箱牧穴暖朗鉱泣肺孫飼枝熟恩毒往豆晩陛径暑拝妹氷棒寒帳肥糖姉脈拾俵粉漢糸綿才銅鏡覧奮眼蒸耕后巣班潔灯麦鼻詞胃寸机磁芽灰垂穀貝刀弓腸皿舌羊絹笛尺汽蚕'