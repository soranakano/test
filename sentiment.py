import oseti #osetiを使ったネガポジ分析です。sample.txtを任意のテキストファイルにすると、その文章のネガポジ分析が出来ます
             #正の数字がでている場合、その文章はポジティブな文章になっています。負の数字の場合はネガティブな文章です。0の場合は中立です。

with open("sample.txt",encoding="utf-8") as f :  #sample.txtは小説の「走れメロス」を青空文庫より持ってきたルビなどを消去したテキストファイルです。
     sample_list = f.readlines()  #各行を要素とするリストを作成
     sample_strip = [line.strip() for line in sample_list] #linesでは\nが含まれているのでlines_stripでは消去している。


analyzer = oseti.Analyzer() #osetiを使って感情分析
print(list(map(analyzer.analyze, sample_strip))) #sample.txtをlist化した物のポジティブ・ネガティブを判別　0の場合は中立