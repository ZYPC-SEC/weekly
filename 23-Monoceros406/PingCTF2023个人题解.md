---
title: PingCTF2023个人题解
date: 2023-12-09 18:49:08
tags: CTF
mathjax: true
---

# PingCTF2023个人题解

## noodle-nightmare

对文件进行拼接：

```python
files=["spaghetti/tjzqohinnyywacrdplxojvooeckayonrdmaycbqcvvxbkibbvv.cpp",
"spaghetti/pypqtzzchhewyfazdybbzhhkyonlnnpuwsxvydmbukjmdxyxfs.cpp",
"spaghetti/xwyqezbcclhfyrrruglguuonewdbimuzajxwwospbsybsxwily.cpp",
"spaghetti/ikghukiounwtmfdscnlbnlfsyoyaymeukjucbishgfsshamuho.cpp",
"spaghetti/ksplifqbplipxkaitfhhnskiopcbrkecqjgtnoweshaeauujue.cpp",
"spaghetti/qwohdckkemgarswmeodemdwgkzwypkwxvjffcjcturidajmbnk.cpp",
"spaghetti/pzoipbuttxofvxezfiphcjnszofrgzwjgjnaomogetsoxsarhy.cpp",
"spaghetti/hmnqzhbykgeulqjjhthltwxemxfkvttsdlouoflgypsoyuplyi.cpp",
"spaghetti/ewfecatxwlwbtybolyypjotvxhznrrktapbtooefkexcmzdfyx.cpp",
"spaghetti/spzsrlbfognxydflsudbnazfsluuilnzrwxbqckugyhthoukxw.cpp",
"spaghetti/fguyfqgwheqnziwylsnarvtwlmkdaiqvdaphtzczdxdzwrmhpf.cpp",
"spaghetti/qdcfgiblfknuuycjgpdfqvwsjiwcnhoczfzgudfxanlipmlnva.cpp",
"spaghetti/ntkmoewbljpqkxwinzdeehytacxnrnecahvvvmeiorwhsnfjlp.cpp",
"spaghetti/uclwfdyxvvpquxfrauojmvprpxkgfyemubqmipzztemlnxxvsp.cpp",
"spaghetti/crmubmyrzwxkzozrpzsfnrrqsgxyvwcuapragivcdpndsocrbb.cpp",
"spaghetti/iqazihugczshgnmrwqleuvleefixwpgiizfouotunehwoybluy.cpp",
"spaghetti/soyuejoqyurpqejhaupxqoaktmdtyqzxihfmxtsrunagrmdmjo.cpp",
"spaghetti/bjzfoagpimyhoysgnvmkaxchaprhkqneeghgftkgeyyovcjcig.cpp",
"spaghetti/hmsbacsmwrlsqqigtyococnwrpioujxjcomrgoybwdxlpgbokx.cpp",
"spaghetti/cfzpdvcdtokibprvouueypprlzhplrockoxnhyybybuhyshmtt.cpp",
"spaghetti/rpyottujqrgppymotvqrwdsnqiwmoasgfshvuomzygrsqscayl.cpp",
"spaghetti/wmigbymrqkfmfzacszezqatqasxbglnjrkvzxdwrxypnjxbloh.cpp",
"spaghetti/uzazhqwthshesnfqymlbshltjfvcbpbmnomujxptaokcncdszu.cpp",
"spaghetti/wqkkrlnyxjyxtdbvgijhbooigfrscnxjuafxbeupyyasafsjdh.cpp",
"spaghetti/pgafltxftijintybmaxnwtvypanhopguztyjfcytdloscdevsw.cpp",
"spaghetti/zkqmrqcxiobxthzwjfgfuivekqmyehzvlipgynrwukybmbxunt.cpp",
"spaghetti/ihnoxlticbgojvlplxstykmakfxfxxscvtvcqbpcyngyhbpcjj.cpp",
"spaghetti/bsaegvddkukumjdajeqrfeuuuhylmzgqgaochtaqklfaztryqc.cpp",
"spaghetti/syoyvufuvokgzaujjsqavzuesagegimyhcjtkjolsguzvwltfy.cpp",
"spaghetti/ohtljaxhkrchlcyvxuaofmtmhoxygjohuztffknbojvwpsujob.cpp",
"spaghetti/hpmjptbshrqagxotpvpfmoeietnaynmctmizvvglxpwsbulxoo.cpp",
"spaghetti/btsokcahliezsixkcmtzggerkpalfizmriuyeatuzlvpkpuyfv.cpp",
"spaghetti/pkejtratvrxyxjmqfbpvbwjcylrswlboqoablwlmfskvboxhgj.cpp",
"spaghetti/nzurqvrgjxypsmqlzturhlmkuujydgkewzodgligiutblxtrmj.cpp",
"spaghetti/hveqtijkubweqvqmggdncxvswtvglwptobtjdcdqwgokkgwkxj.cpp",
"spaghetti/hmspqhvxudrzaqrsjdgeegfwwrppvyxickphxjzkbbgccjgaid.cpp",
"spaghetti/neubacybwyhbyecusdcrcsdomzcgwwbydwyvtrsrmhpxrmhfkp.cpp",
"spaghetti/fmwfjnhpoitiigpbedxqvfixdaqivxamtuaifleuqkqkwtxsfw.cpp",
"spaghetti/hjfnebcdxlnzmiynlhinjwvqsbfvorcuudzgffvknljzjlchjr.cpp",
"spaghetti/axpggcaaqgqicxhxtscvagumyxlgtxusnsvukdbvmtugcqcwcf.cpp",
"spaghetti/kqxiuprercmgmjmjcareibittmjdxhqoodkdgvnijjkkyzvyln.cpp",
"spaghetti/jzlezmnuloladbumtyposzexmdtillhlnrerchaplfmpfqltfh.cpp",
"spaghetti/ccmqhkwtsunsausxybgoaxssypkhmqogvesziruxrakjthmlwp.cpp",
"spaghetti/repnzejizoqlpsfmlrwlakrrmuhwetvdxbyitniqswlspceueo.cpp",
"spaghetti/etdclkdtwblujonakelnyzvuzjwdxrtsqgdchbwrqtvreeywhy.cpp",
"spaghetti/cxjftwjmrzkvbljrvfvstaosmnoinolhjjupfxtcqwndlwsdow.cpp",
"spaghetti/kgvcqvswbomrrvgayosgonevjcsptqkvrjnlxtqcoxiillsefj.cpp",
"spaghetti/kfrjpfakjawzfdlefzxeyslcalyiumutzdmmuvraqhewyuskyn.cpp",
"spaghetti/vgoltirohwlcuejmkhnvkoopjbjpockujpvtwmuzgfobmfboqp.cpp",
"spaghetti/ykmpqeliraifkcvjpivlcgzehmxzetaggwzptzaglqpfmbocoq.cpp",
"spaghetti/btopckeyzlcosdgihyodzmirestvkfmxzhefjkcwzdhiboprjp.cpp",
"spaghetti/izgrpoafquaqswvvlbjkmvilttjvrkzobtgdfwdiszenemawsc.cpp",
"spaghetti/uthowupivjewtdjlligstbirfsmdyifeiynzwxvsjzdaeymphs.cpp",
"spaghetti/vnjeyanjgjbmbetgaowaaambztbshnnkxgrqdccluankznaoym.cpp",
"spaghetti/xhurgrflsfnkccqayornnltbcveifeelngvscskinjelcblcuh.cpp",
"spaghetti/oynqsgkdccicvxotztmrzstrlxnukgwclnudpgdimdduvprbyx.cpp",
"spaghetti/zdgvpeuonlzvykvlhpwgsjesgeplgajjhbapwzladdhkpnufoa.cpp",
"spaghetti/alldppndgicuqwdqbbbklmiclkzpcleoptydsnklbyquiqwaly.cpp",
"spaghetti/fdmcizqjuofplccgbavkigiumutxiryjwgvrwvcoyywohcpgjb.cpp",
"spaghetti/ftsiafeqeynzweicdckvjmeuqlsqjfynhbabkfzkrgkjesmelu.cpp",
"spaghetti/uurxlwpmjrxhoagaabtvgcyjqgjfqoslttlrbvukhmrezanjbi.cpp",
"spaghetti/tmwehhschjxaobuwpivtmktsifcttgajfjoqvzqnwaitqbgxoc.cpp",
"spaghetti/tvfpdoziysulibvtkncovvlrlwwdhptqffuwdjbctsceixjcjf.cpp",
"spaghetti/eirnmftchtljjyewngxsrbkgdjzjxvhcavmfprrhiljsnonpms.cpp",
"spaghetti/csytxxppykilsevxjarvojlwfwvkconbixdnmaqoryomwtiopn.cpp",
"spaghetti/uflkirswmlxkmhmfvojbjsdszrniunahmwuxtasfcfnfjecyoe.cpp",
"spaghetti/fvvcpyukfekvjmwnumbhroikkhbqestqumbhvlfngmchyeahpo.cpp",
"spaghetti/hddmfmylhkciumgzbuyugavhdpfyobywlzbzajbzgfdktrnadk.cpp",
"spaghetti/eheukmdasryspfqadbbocwmdmabemqcfioifezdtbbwdxwyyzi.cpp",
"spaghetti/wpgnlparnbfzavtwedkgklmxwvguaruotfbeoegwbrdwvrnbgf.cpp",
"spaghetti/pimlbhlodwgefbhgxntzjcfexiumnpgiwkdhjgejlrkoakjhpp.cpp",
"spaghetti/moqeopqthkxldydlonftmhjnfbxhvfnmsxgbmlzaxdbycmwayo.cpp",
"spaghetti/fpkylumikhthawaraaeyibbufmqvershzorufvkftuzyhnwtex.cpp",
"spaghetti/tqwfbpujhydrrpbtocstjshsmktrbsuhnovkzvfayylqtqmlmf.cpp",
"spaghetti/mnoefxtfsspfmodlvenznyxhibwirrqctlysoxtreweloaumhk.cpp",
"spaghetti/iutgcjczmuetwdspgadmtqthfabdfniynilamagekrgljzgntn.cpp",
"spaghetti/yskddnqxpdfcgrrkqsfrdmhrvtopbcohlwebdxcbhyahdhhlfg.cpp",
"spaghetti/hlvzgmocsekbceburtxobmytxxxnqxxkvbkprrqzcfgukovqiq.cpp",
"spaghetti/kxqtsoysubfqtslxrnxneebptfwdwrzlysbpotlgkertrucdtz.cpp",
"spaghetti/nnpaeoycppjvdxteickqilgfsqzpjgtpsyzyvfqwhclzpjzzfn.cpp",
"spaghetti/sraosqevpafonmctwukgxzqevduclwunpgtnbzsceysxzrsyix.cpp",
"spaghetti/mwthfslvjhtnewopgvuzlzuqyktvuclezlmdvfldlntuuknxud.cpp",
"spaghetti/raxkgflwnkhdfkocvqyigljpbwhwmibgdbsfsagbqidwsowkiu.cpp",
"spaghetti/waylkzwxtgbidmkdweqcfjqidbowczukjouljtipwqlvigevgl.cpp",
"spaghetti/ihoofolunrlvskocsywoukosinnbkpaxzuzhftfxhshudfdkao.cpp",
"spaghetti/xvahbtjjvkpqzrkckisvayqpefpuvickvnotxvogaxitzxbgwi.cpp",
"spaghetti/jihvznizyitkfczmiafpgdkfgyaesriwkrytlwijmgvfpuxgvu.cpp",
"spaghetti/lfjecqkeydvtcwlfoyrbpdgmafzxlopiakaqjakibldecjubdi.cpp",
"spaghetti/ltmzkcfhwjlrqkfffxxxcoqfdzidyuvfjaokgygzcljnixicbz.cpp",
"spaghetti/bqzkgvffdfhrszqlvnninakcjvhqbeijzwfnydwwtglgykxhzw.cpp",
"spaghetti/kllfymqihabfltycymgnlpiaxozxomcotxykjnbpobwnuljzoe.cpp",
"spaghetti/wyzjoqsonxvqilfmbnrgwbsfeiuwaxhozjkzuzfgswfihisfuu.cpp",
"spaghetti/sbouurxiuswzubxyfeolqkdpubziwlueafsmzykssipqfxuvxo.cpp",
"spaghetti/xwstxodrsgxitnhowavjvbggovomemfdaidradueaztxzqitmn.cpp",
"spaghetti/cjtsekntqwpurrapyydbhhstyoifjukwxzxabxpjexntrmugsi.cpp",
"spaghetti/husvzrwzgzopxbbebtoogaditolzykyjrxpizqsaveauzopnls.cpp",
"spaghetti/ncndrcvamcclegwaqngwqwbqcafubaddhqxyypztawuxvuvphg.cpp",
"spaghetti/mdlxkhewfyeasmmnyehnnetgvvzvopzqjvwyoqbgiwfrxtcxqh.cpp",
"spaghetti/otsyiqqbeveloechnlzoetjgtktqikpyaubeqxanztktogcjhj.cpp",
"spaghetti/ehkcwmkcmxdgaggpavmiqupwozpgodpcarsjjwrzglhewrcyjn.cpp",
"spaghetti/slidvnryjourqdimheqyhnvrvauqmoyrkjdwzhqlmjftbsqoil.cpp",
"spaghetti/vqespsipwgmtpybzugsehuqmzgjykkkuymiemdxkiqtcnnnykw.cpp",
"spaghetti/pgxhrkwyrbfvmtzsxoswytkqrfqcqcgenjcayjbjsmoemvpwll.cpp",
"spaghetti/qibumayhwudagzgftdgwoviikvfffiqnfojcbpadrfdoiqmnof.cpp",
"spaghetti/dajuvuvjorxtynimplqoapbufoqevatxgsjvytuthifqqfgipb.cpp",
"spaghetti/fdrtmaivigudyfdgiecnqmagssejmsbbsnonbgpafdodqkohrm.cpp",
"spaghetti/uwzorjuciejsybhxcpctyxiltbkfoakxzweyhpjvribpushlpv.cpp",
"spaghetti/cjlgzivlztepjbzdggkzfjiumzxtogypmhwasfuquovnsvpbvo.cpp",
"spaghetti/vlntppidbnocskivishdathudeonivvzxwosgqhfcldfiyikpz.cpp",
"spaghetti/bwfgzqfvpkkzfqejtvwxtgsfqyiapgpblwbdetwugganfjjczn.cpp",
"spaghetti/wmqtncdunukufhgisrwsvcrvkeilscncgibwqldgvypbxkpgew.cpp",
"spaghetti/dquruhkoudkghasaacmdcqftlwbwmrbkxxuupsuxhyiuscuzho.cpp",
"spaghetti/gjmmjsucmhbthkxajwvjeoeuqihdiziweniqjqqgfyvkwvbgxi.cpp",
"spaghetti/ezeooitkshcihtopyinnyqqhudxbikffpxirkxxijqljfubgvz.cpp",
"spaghetti/jbxozdrdcvxwwyxztofsipviqpcpbavcpjhbbvhleuoluhmrbq.cpp",
"spaghetti/pljsvhocsjosyezyukotxedgeafowtomfaowtwrxpichedmimx.cpp",
"spaghetti/tsxxjyftdsmxkmnblcxuzbshobwriyaktpcxrrrrrarlbrzxyk.cpp",
"spaghetti/nnzqptvkeadzmbapmuaroennmymsjvnidurgnebrrcvzjabhkf.cpp",
"spaghetti/tedencqifdfedffsmsoqjgsrgaaefkkyfdiaijcqwntgfibzbt.cpp",
"spaghetti/styvkckqykzqxsivfqibekrcsjsahjnuyjikutziflevdqwxyp.cpp",
"spaghetti/jkikpxvxsxzwgweqwfviepiylqialppwbjwfvmqiywlqenrlit.cpp",
"spaghetti/tgxfykdcnabiooyhtyjfkwysdzrrqskwcjcaaieldnejewldxc.cpp",
"spaghetti/evcucgijsxpsurosqhcjnxyrihgrzhvdixgthdiznhaadwandb.cpp",
"spaghetti/wahvlnvxkkdfdmhmbndppmllybtsjdwxtcgapjatbcqogfvurf.cpp",
"spaghetti/ecqploqrjrwmkxujydidfxrqllvqqnflkvvttxdeojdmphiosk.cpp",
"spaghetti/dwbquzxfspvosalsntucpztkvukpecgpaaffnscqvqmjqwhqdq.cpp",
"spaghetti/rytysvhpsshnqujrfivwhgxfepdnfmflaxhkdmhbunpvsnkcix.cpp",
"spaghetti/orgjolhmzzrajyarmlbucfjgshjsfuartobcjojwpxiudrzwqo.cpp",
"spaghetti/zhxkkgbshlcinugtqhumfmkwnkqdktrqvvbkeltthoyltvbxuz.cpp",
"spaghetti/zeonxusdenewiiaelfvuaonfbzwwhyiabldpqjdlouwbqelmdo.cpp",
"spaghetti/oehtqjtzmvxxesgjfonhftsuliuqlixwqkyhktgpxwnpibprxm.cpp",
"spaghetti/sarrwfrlxcsmzfjxzjovugonsycmxfhckblrifweliqndxpsmj.cpp",
"spaghetti/ybcqlfqpsfbfeexfmdirixyffwhyobjldxwgzwdrcqxrphwypd.cpp",
"spaghetti/uuuqggoyjqgkyvxlbeeipfthtdytatxvfxjmngbylfqdjmaofd.cpp",
"spaghetti/mkhwklcwpiynaqegeohkwlxpzvpxxjjiipkrnqecmtqtbkgybv.cpp",
"spaghetti/fvtdpgwteltlaffageglatgbmnmfxqhchvglzufcuflfvtmrcn.cpp",
"spaghetti/ktjdfhmbpbttsjqtpdwotgblvuwpcpknfrspgxpdwzfghwbxjg.cpp",
"spaghetti/prlpetnwzctalodbgiphevhmrviwxbmfnlxgoqbkbhdffydkch.cpp",
"spaghetti/waizgjycjfnnwrbnyvhiwibeixkzjjbutjzjizydhymxvhnjck.cpp",
"spaghetti/tvxfvpwytwoplyrsiclwwocashgqpodopmvlklnnckankxsmsb.cpp",
"spaghetti/ozloodrbjqsfpbvrqmuxojqzsviqzqhizpjylegxoxzstxtilu.cpp",
"spaghetti/xfpnuoxoyglsotudygdvfgpmcenootcajwxgqamxujegyinvsp.cpp",
"spaghetti/ndehrvbpvlqoxggycdvznbttntfzcgxwtesenrcxgpnsuzgqac.cpp",
"spaghetti/oqzcoyoukhrjimapoizaqxnbjsxarpwuihsjrofakjltuzxmpy.cpp",
"spaghetti/wofwktofsnzybgfigjrvrbikbeuzifkxdfglskjwkipbwzwxvh.cpp",
"spaghetti/vfupgtmjlpypzymhwygonmtazgnnnjwlvbfdapiviihbksdvsz.cpp",
"spaghetti/rvoecjisnwwhbelpdpnrybhderpahzplayoctjervllcmxclbb.cpp",
"spaghetti/mtpsqgezksgtjigfuprbiexopkplfsuirvxwmpbirzrdqrlqqa.cpp",
"spaghetti/dvigbcuvlkctojemcyxzhvhiqjicbffrgrwaitqofcpxgjrwph.cpp",
"spaghetti/yuejbikxqcvljygbtsnkltpaxuznqndhuroxhhtypypqgnyuez.cpp",
"spaghetti/iydhsnnxzygigtwrxibgwtaxbqsvjhsgneqgusdufreajvkqkv.cpp",
"spaghetti/huxuflehxytlazchvvbmcffevjjimwolhprotardqeisrzosvl.cpp",
"spaghetti/xuzygfpqdmtxefgrmyamcabjmcrnwgrqptllczdcvkdmjsshzw.cpp",
"spaghetti/cddvgkwqzgdntrlvzavntltecnuwwrvkdlppzffddkpqaqgcjw.cpp",
"spaghetti/yurvjyseeamxwpgbfupzftqxuceofhxosyyrgpyxlofpneyvyj.cpp",
"spaghetti/giktbzvnxldwtkzozlhdleszokksanvhrqluqcdvqeqxguroaj.cpp",
"spaghetti/oringgzrlamwzwshviefiiuwsutuzoqcevvdllljlynerarqpt.cpp",
"spaghetti/hthamorrvrpfbhfnrrhkgbrpvyamfyqfqgdegzodysnokrhman.cpp",
"spaghetti/nwnbcycvilsndunjyynbmzoynocbvtqfxgnnrjfjkrwywpwnse.cpp",
"spaghetti/eopornyfeawbbdxavfxdjmnzcmxhccnmvumeuvaircsvwxnzdu.cpp",
"spaghetti/rxkrawbttrxcntwauaqjmxxynknpcfbalgpigqgumndgqihqgn.cpp",
"spaghetti/cciqrlwvnhcrgmbdexqqvaihfevbwktfoslbqrcgpdqjwitxux.cpp",
"spaghetti/yhrsgapuknrfiebjdrvkfiobmyhfexrivmparhnikuhhqsineu.cpp",
"spaghetti/jlvrxucbsllkacpqljufolnsbsrforsyxwlryrkftgqwktqymf.cpp",
"spaghetti/ppduzzkpgwocpnyhrmzlrebruqoszqqoitolzrtgjlyssrzunp.cpp",
"spaghetti/lvmpixokgkgilebsznqjuqjanflewvxivstijwrixketmcqjpw.cpp",
"spaghetti/opmqmsaltrudcuczyphwjkuedyzumpwfvqdlbgwblwjbxezcsg.cpp",
"spaghetti/pqxfvyuzblkfljhybghkusvgicrmunrzavrqrvkgolkgeiqzms.cpp",
"spaghetti/zmaxarxlzczlwntyzcmubthmsbvvsmkgttavoauvkbbycynkiy.cpp",
"spaghetti/cwxedbcdpdwijpzzbzmwbmlfcgvlsknxsdlrjlrqmdastnbjim.cpp",
"spaghetti/ypbrzuxjmebdempdzvgynhsdmluaanpmlrxpsvpeewdduskeqk.cpp",
"spaghetti/dyffozezioboomuzephpznrweshadylbqjtvheobbgnihlutwc.cpp",
"spaghetti/rggtlbwkkpaklxvxhlbryqalukfukhjriffdxeizcbhojxrzry.cpp",
"spaghetti/yqtypuhaszfanunsrwzpeliswyttwfymqzgxryxioayudnzxxv.cpp",
"spaghetti/xscqgainvdkrgoyoxuhmicdxfhivszerakqminhjizsyqsdhcx.cpp",
"spaghetti/frnbsfdhrgubwrmqnwlfkwhxftozufqcvffwgxzelejmoymmhh.cpp",
"spaghetti/ofiociypwdypfihzxbztqkivkvrsweulrtdogqbfrydsgpwffa.cpp",
"spaghetti/aihlrlxdjxvczdkisqszbhjmesemcophvutnzpfioedaakccha.cpp",
"spaghetti/mipzdkjhlzjrvmsndmzskuzcmrclpcztlczihrvfzsomwywspm.cpp",
"spaghetti/ilzmmstnxmoioubpldgypxpmsfkverekgnsqtckdpwwropbram.cpp",
"spaghetti/adstpgpuygszvrvmkkizqgfhkzguuzaadmpsiuzuugyjywipfe.cpp",
"spaghetti/glgnmpcewxeohdasvoatzyqvmzhrchclofkafrlgduuecqnhos.cpp",
"spaghetti/zgfplmhvvnmoujgceorgrvqkctogznyzucfcwtiugpgepcgfqc.cpp",
"spaghetti/oybevqvtjlsdhfsoqxwtwqjfbiwfothdukjhldyacypduoohkz.cpp",
"spaghetti/xbaktmxdpzffodipymftumorplwxhogafchqvtlcuohhnhqsov.cpp",
"spaghetti/nkfmnbopdxmkwdfvizyoesypbbnhpiucbfkihwgopgkoytjwbf.cpp",
"spaghetti/fnakltwxzgdelyszbkeedncckbhfmeojtbnjqscekichdjyrab.cpp",
"spaghetti/fzyyaptlhgvbioekpmygkxmcskpocsmytzckvpqairxkvulcoa.cpp",
"spaghetti/nwptxiiufxyqgqpeqbdbloorqhknhlttxlhdczwvvfyxctidnd.cpp",
"spaghetti/fophmmqzrglcoritylaingbpddunacgmifyzobbqqkwxxmskie.cpp",
"spaghetti/bxfhfuddbsohtbzognuyugbuxbelldhhgexrxricnxnrbgxbxp.cpp",
"spaghetti/sllhgzrqkayquceibusjketzxrwzgvqqfwfvydxpjewcmgsbbj.cpp",
"spaghetti/vgoumuewmarfvlainroxaclazblwjkdqfgyynbwkjgjojblgfh.cpp",
"spaghetti/avdnhuvnjelkjymvfzuzmhwwbnmqkelnbiczbgxsdatkgxwzmv.cpp",
"spaghetti/ratxsljndyfupxrcnfyxbyvgqtrvatwuiuiwcbovvhoduvdejg.cpp",
"spaghetti/jubpimicklwoicjyoejtwccayfzbwfzcabnzqgueqrjnbpafdc.cpp",
"spaghetti/iniihtkpxokjroqyrpmipfcebpltquvwbbjkwzvscrmffqxlfm.cpp",
"spaghetti/fzuxiohohxmonysnppwvwcapzgmogtocqzqskgynbnyycjswba.cpp",
"spaghetti/klpxtjcrszbcxiosvuuaavajqhpinlsbaldrknfevjzvbvuryv.cpp",
"spaghetti/wudsenasulrcxegsamicdeqprqspyucpkpilszvyhtiaojfotw.cpp",
"spaghetti/mlofwegjksrldkuxfcdtsrnifxkncshapoopqennvhovaqdoqi.cpp",
"spaghetti/wkjdcxngxygtcxpiouyxbnlgshzectbfvjowxeibivltlmzgsq.cpp",
"spaghetti/wsghevfralwjtlykilhqhhyepkrjzmozfspsmsjieinhuwpcqw.cpp",
"spaghetti/nwihanaqvnhgqeszwdnsnuurcaaezxnjdxaeqttkfvotkcivrj.cpp",
"spaghetti/wedslswcsjtwpclraadfrlnsupefujaonvchwwgdgesbxzozps.cpp",
"spaghetti/lwyycwulmytmmktiedqfdtcjgmypilbhkvxgdtegcqvxbfcqms.cpp",
"spaghetti/ngytslboprjksvyhbyqmthquxhtvqtqhsxsqfevgetosldgvsb.cpp",
"spaghetti/ampuoppblitsjihslskzquzrywbbhwcpndllnyvprxhnirwate.cpp",
"spaghetti/uzwhyayjycuvkemiceojdorlfkvvqoeevxntgihfbuowncyaqz.cpp",
"spaghetti/cuontyxpvcrtqerkymiyosoaogdsuajpzzykyckcfpnkvjeoek.cpp",
"spaghetti/qgewajjzizrrdrjfntgwdyvsieeiekmkvnejowdvwigtsfmhxg.cpp",
"spaghetti/haxiqakmakffdnxigpnewamwmafukrhwdynvmsrloznhrsqlsd.cpp",
"spaghetti/pgotkchnktgmmjrcyobxmzxdxxcvxhvgmicuqdxrebbyahijvh.cpp",
"spaghetti/mdnwigqgxxzyrrhzjzwkppromubpdgkrqegbguwnixzhrqnwrq.cpp",
"spaghetti/lvpftemkiwtmbstiduflkzzgsscrgdmrywwtxskxlwnblruzrn.cpp",
"spaghetti/tjyececbpaoeyhvagabvlsozmtdjypkajxzhkzxohnemjmdnqt.cpp",
"spaghetti/mhwobvsayzkzhsvmjxhottwwqylagmdtxnrqnxffhqqaqfycpw.cpp",
"spaghetti/zojyxsfipcesugizlwhptowctgllvrbnhzygpvdwahvicxmllp.cpp",
"spaghetti/gezbwfqbroufqacyvqoybbgszzhfrijveosajdgxbnoqobmtdk.cpp",
"spaghetti/xuxveveixraythmufifwnuweqyugaciyxssudcikpbvxsbucox.cpp",
"spaghetti/rbtgoxpcwsbbvhcxsjlejgbqyakovfgfqoskdgoudbmobctzmt.cpp",
"spaghetti/icwpvvkcrlwslkvorbskcrqrljvfbbphtlkajykutiqipfaihr.cpp",
"spaghetti/ufsfkuzqitcvvbmxtgybiuzlcjdgqhcvwvzztzwxphdukczpld.cpp",
"spaghetti/jntnzxrcnsbdlghgekquorlrzmfhpifsctachzwxeldxwkpgvk.cpp",
"spaghetti/kblvfwvpssypwnddnflwusilxgblovgxxxftmkqxwxervawpwf.cpp",
"spaghetti/bbufdmujorcnyobnpsqdfamkxgcambevfxmspiyhkeavcesmhx.cpp",
"spaghetti/bwbliibackjirxhgqalvrqdacsmftpxxlhswaddfnntrxcnaqk.cpp",
"spaghetti/jiznkuzyqnnyogcakahnnrogolwphzkqhlqibrumjxlgqqndzh.cpp",
"spaghetti/nltuwsvovnnbyyuzruptdtbkacnsybwerwixhuopryvlidocqr.cpp",
"spaghetti/gosravmojqimxdmzicpcuxrslaqdqctetursdxckdcmepjrrce.cpp",
"spaghetti/rmtluplczfuljozpofrphlukpddmfjiizegbbzivddjfpwrdcr.cpp",
"spaghetti/xfrdlxqwwnalcatwlbnowtsldnzhtlllgltggplmldwjisanta.cpp",
"spaghetti/frptkkujjbbumvhtpksjbkceclpzyrjlqpcqpzfahxyzoizfkq.cpp",
"spaghetti/uerihkjhdcbjyineokzzgcegdkahrxsgjhqyjoiuojuajidqmx.cpp",
"spaghetti/vouesxookdgiwbpexndbgghfogzkhbnccwyhilmhxilrjwubdf.cpp",
"spaghetti/yjmcirqjeljkcqvumysqdbsyrspfdaojzclrnnpcergbrgnlhe.cpp",
"spaghetti/ukknoqfbmhbdbrjmfmupqcxlvtvkzlzusywhccksiphrusjrdu.cpp",
"spaghetti/mgflljjhyadpmyfwwtimodpgieifiqgcdxlelsxrojfxurjryc.cpp",
"spaghetti/fjdxhjclajlpkxeexfqilblqzkmlbrdexrluigacysijgmkkht.cpp",
"spaghetti/abjhpkzlvkoxakpkmumttqdiuxqcbwaohrlyttdyrwjucgosuz.cpp",
"spaghetti/vztlyrwmdgawiskpxqkvgdkweabcxfpfkenxmbvddnjqhadiwx.cpp",
"spaghetti/puwxardezfosnwavxvzzdvssuobluzzuwhdbeamwdykmlgzpfa.cpp",
"spaghetti/besbjhaewjjmkigugwxxgdjvhlvispbkganusyvwuhdrkmqjij.cpp",
"spaghetti/aoussaasimomkkbhiycxossxxhbnzbdxhxxmoacxbkyhkodagi.cpp",
"spaghetti/wsasatazywgdimftwdqfkaxxpciwabfiesgfpjhsvsvhrgalom.cpp",
"spaghetti/yhgukerttxrthqsqcsirujdnwaubicfytaqyvklrlmlouzdcys.cpp",
"spaghetti/yaaagmeplurgirnrehymcswlmvomqympkpkwnftybfmlieodsh.cpp",
"spaghetti/ocsfebrsfhxbyhwjbhonzbpzkzldcypvwsrgdjosuujxwbzrek.cpp",
"spaghetti/kxeejacnxeodaulyilmyiwnmvtwwtuaelxxlcgzwzsdeelivko.cpp",
"spaghetti/tnizshkgwdrmbqpaemfahmyrsuhousgpqngckgxztmsxndbaih.cpp",
"spaghetti/pzhlljzvdmsndxtlcldgwlzvubsgqvnxjhnatlewysowbnnapb.cpp",
"spaghetti/oagaxkjcumkovvglenqtradzrwjzdfshoypmaxvldvqcppxqlg.cpp",
"spaghetti/ydtecufvkqyoqomctnmwxooxyfwglxapyikilpywnradmexjvd.cpp",
"spaghetti/vouxhnzagtawvobkrxswwffozmmbshewuprpqcxzvcnuvypbzq.cpp",
"spaghetti/oahkltgvdbhknpvhaticbxpxdvykhjuvakrlifwqwwkthqslaj.cpp",
"spaghetti/ggrqqidaureotqwbxcealoguqhqajiainmodjjapnkqdzvivft.cpp",
"spaghetti/rildbbicriftffvukugmupmcokyxzdjkwohaaqelekdngirply.cpp",
"spaghetti/vnuuqkknrcumyiexddgbpmkgzpnahbzgmbpilhceowrbwepfpf.cpp",
"spaghetti/dyvvhbajajtxfdpfmycpuucmagfuvzxryqltucxvqffdokbdlq.cpp",
"spaghetti/rjefhjscbuosaugjsexbubghcnggfxbbablaseraiwusflhilh.cpp",
"spaghetti/rvtigabhzuxlqmdyxvbfrezxwlddwzvyoqbrkmqnxtsnbobias.cpp",
"spaghetti/hwcoujebtkxitvgqncaibwsnuhvnjljutyoowbnldciaozeeex.cpp",
"spaghetti/rjcawiukreoekycvuynpvoljpwbuhvfyiyrqmtfnmyqfnwrvtw.cpp",
"spaghetti/wftirwwdelebqizcjinabqoaazwjctscufmedibutszivdshys.cpp",
"spaghetti/nakrhiukvylugacxwlfbmtbyriwzlmjpcnqugjmupyrrmyaziu.cpp",
"spaghetti/skplgestdlylktegqvuxbhxejmylzpmmmgkiiyazfdpvwqrptg.cpp",
"spaghetti/hkzayynlzftcdyvocawfgsaxdvztfvkevwcsaltektyjjrpccx.cpp",
"spaghetti/ihicbkrxbbozbjjjtqmpjyqjizdmnxcbyjnlgwvlmorofrazqa.cpp",
"spaghetti/axbmnoauajcrwrznqxlfychfjkyelbsbfztrxshhnvqyfqsncx.cpp",
"spaghetti/owzfayuijvlbjgrrybzhcepkfybyzstkzswyktoxqmfyyblyps.cpp",
"spaghetti/gtvhkoebufkwfdorykesjszuifvcyeyudogwyunvcybpeorxax.cpp",
"spaghetti/jqvyfnncicnugpzwqnvxcpzroetbillskvmpmlugpwadkyqxci.cpp",
"spaghetti/lnpmhxymcvwwiudxdchdzkkktytruxnyluhndbgbhvwvdsdxny.cpp",
"spaghetti/alfgurnlfbhtbnkonhjztbiqmiviolkdsfoattjvhqlvkltirf.cpp",
"spaghetti/pgfbbhtmscucbumqyfmejjjjxcsyrnaervxijcfkebraucqmxn.cpp",
"spaghetti/qptcdamtstoxtnpwzlchtdcetjlnrtcjqjvpasqeychhrbhfvd.cpp",
"spaghetti/ilczflwaebdpceorzgwrhnvkaqusxrsqtdvusrsizobywpyrbv.cpp",
"spaghetti/yhcajwolkrwzyyriglxmbtqagjphzxckgbkalzihclkmfzqcfp.cpp",
"spaghetti/yizmrxkbkwfwkzranitohqdfowgvqlaqqtpzwuncokppbhlwsr.cpp",
"spaghetti/xikiqjnkwcdbdrjytlilzfqpuznbdzbjefotytquwvghqmxkbf.cpp",
"spaghetti/ohbqpuxzgurdfwubnsrffejvdbnyatbhvfejlccsmebwnnqtwa.cpp",
"spaghetti/ixjapazjvmsuhfrfyhrtmgjwiazbsecrbzpvtkfiqxhogaurzz.cpp",
"spaghetti/ezxiocglvjywjnneddfodcdnhtibguxukrpqvgggkkjdjunkyh.cpp",
"spaghetti/prslazobjlmflikkckpytltdrcqhwdrlrfokraqryrqgobgkes.cpp",
"spaghetti/rufrhreioxuczpfircwofokjnwaachspdsbdohfbbocbfoydnt.cpp",
"spaghetti/rikkxahijvghhzzeckzjcyoawibiekuzgtwytdsnlpebklgvtj.cpp",
"spaghetti/ejhreavpafujdfodobgkhpfpmnltohbxrbhdxwgjukmdbhgprg.cpp",
"spaghetti/qhebxfmcxonvcyeudwyngfipwpxlhrbxjvdrlxjuqtzkqyiajt.cpp",
"spaghetti/vyhdouazklkocpnvfckzivezogttqpanausosaitkaybzbhwer.cpp",
"spaghetti/moanwsapmlcijsqzdzyxekmnhebapujbhrnuirijjvbscfhajr.cpp",
"spaghetti/aknflzkydoiszckudtoftajnknykyjotpszuugdnzvejqlwmuo.cpp",
"spaghetti/acgpoytkwegzlcdvvrpkxxsvqocbaelpfsupfqzydsnwunvnyi.cpp",
"spaghetti/mrxjzydlekitdybqrgrgyhveovtylqokniawgmlnxqmjqkzqxj.cpp",
"spaghetti/yimjppojhgxjuamipdzuxsjznbztkiohdosefeupngsfnqcgnr.cpp",
"spaghetti/iqttoeceatvkvvgkiaqzgxupchrthuwdzrbgqhfgvrwtakxqaz.cpp",
"spaghetti/gfppsrxvovgsyfyfyrfxftisvixkkjctactsmmnkkmbetrjeyv.cpp",
"spaghetti/ntfklmzpcrffjofyiwibcwrvhspbxuigselwutxdrrswejgiso.cpp",
"spaghetti/indgxkzlifvytonvunsgwikbjfbprtxiaksowqcfpqkjzslrgg.cpp",
"spaghetti/yzyazifefvqaqifxlhdkgnloiheknsyzgfalfqpudcfwfeeaek.cpp",
"spaghetti/kvepzqmsspotjdswqwodlaadytnawhnjfogfztvfasjzmbqwcj.cpp",
"spaghetti/mlofjmeqolxlnpjvfvokbncnlyfnmcgofpckzwwvpkebxwkbws.cpp",
"spaghetti/jhjsysljnsvsyikrxgsiouxjptjmowhgdsklhqrwykechmbrhh.cpp",
"spaghetti/ronplmlxtmojcemkomrlcmwjkzyryvfdyvrouixuwmjxnyzory.cpp",
"spaghetti/bebiijyorbzdselpxdlocnqaebxkryxmzewiygwoztjdtppxdh.cpp",
"spaghetti/uddrcxkoyqkdhjdepglhvrwoavlogevqbjoiuzpxxkaooepogh.cpp",
"spaghetti/qyeejnkpuxjhskdbqvxjirdutjisyhfsrqmptmjvhezrmamzuc.cpp",
"spaghetti/klukknrhamphkhwimkzvpzssaxkwnpzqvwumiaqknbcmconfei.cpp",
"spaghetti/jahyrzwfcqdhwdfszgmsakydxaiboquxryedsaddvgwxbizdsq.cpp",
"spaghetti/zmpsalxhzsfjzhthnllevnedvvfzutudckpmndepqxnluyfkpi.cpp",
"spaghetti/cmzumlhzvogucgwqzukwzhrswjtkqepdarwfavindcdoerchub.cpp",
"spaghetti/bhsjzimbyaiuykirqneslvutpuspmibmgplopxtnyowebyoaxx.cpp",
"spaghetti/khsulbaogfhxzcmcbamqtnhzotuuguybinnvdnxgcadrdmpewm.cpp",
"spaghetti/yqtekuvggqlzflqpobvqjlifkuufrwgvsbtwwhkippcknyyizj.cpp",
"spaghetti/hrfcgfailhtpjmoqpbiobdovudbhpiveyloqchzllugmsesnho.cpp",
"spaghetti/xkjslwxouqvkfqtcbkcxcgkadfesyqodhqyeejlsssrquutarp.cpp",
"spaghetti/vyigfhexucvctceoldfqxxpfatfkwkdeqjcnwdkigxxtstnuzh.cpp",
"spaghetti/kiztvcbubikavrmhuhkosxaglptniytcfobpzmbxpzzphhuywy.cpp",
"spaghetti/jvhoaxsdzrtwxyyvsgmyoqwjkuvhotvcrxmmztnkbcebntnafw.cpp",
"spaghetti/igxueswwwislzogygjcypsbyawsnkitckjfonuwmfodrgwqylc.cpp",
"spaghetti/rwdqeempachkiopyhewogfbhgwytwkflknyxnjtfzeqfqrsrzt.cpp",
"spaghetti/olimwlhvlpzgvsjboziizmpyikzlysjokktrooqgndfgnlmota.cpp",
"spaghetti/xciqktroxxkwsnvjypydvkweouvkwcwybgvlypergjqeqbqdry.cpp",
"spaghetti/ypaeykpekaeuuxikxymfcyeeyryyqogxyyostgmdkdqmuwqdvl.cpp",
"spaghetti/ijikprkoqqvlaofplanbbskslqxqupqzxfnslwcxqufmsaeiof.cpp",
"spaghetti/flluoynnopsntybxybyejfbrjazttwqbvhfkphteizvlcbzinn.cpp",
"spaghetti/wiebjuqhosmcjxzckbwgptsxeacazpoumvrgbtneenbirsthlh.cpp",
"spaghetti/ezqrzcvzoovqdvgifpmepauqgpfkvmjlcivibsgrptbhtngqnc.cpp",
"spaghetti/btdayaeyvhpnjhhddnlyktlrhgjiuocsxwuxyzfyrhmniolhjw.cpp",
"spaghetti/syiksteyzsfjkndhbnprpntedaesvneksxzmvzatvdcgxxaqla.cpp",
"spaghetti/ftcckoiqdlcevpjgwotimmnzqenokcdpqcqumivqhtbkyeuaye.cpp",
"spaghetti/ryswavthrchzjtzklmipsuzxqaykbjpeyofrjgbtctgbebsqmd.cpp",
"spaghetti/tcpqfrpfyiyhbdxpogpwqvpazigbdxdyomlsoyzwmrxucvaicu.cpp",
"spaghetti/prfutjyoprztqtgnnvmuiyuczowwgqgrwnujibrfjcbhbipumq.cpp",
"spaghetti/flwqsxlptxetyiwjtnwxxegbguqaldzvxyyohcvsdjrgcwuloh.cpp",
"spaghetti/scgzpqoarnobedaxqacicckvllbcrchttdjsgvcflcezyriyaz.cpp",
"spaghetti/fcfvzozumribpfqxggnngfecsixppbdbxoxjlafdulkfgmaibe.cpp",
"spaghetti/npdyziqmpqekrhdpheambyhisnegexsbdxsxzttpljutnubimi.cpp",
"spaghetti/uvtxlrnfhvexnqiihhzqvyturlthirzlqmuwonbqgcfryxfvmx.cpp",
"spaghetti/bwsocoopydvtabinilcxlmywukssjacoglyugznmnkgrvcuxlk.cpp",
"spaghetti/gjbdrmdtcxroomiyspadyqmopfxljjpdfgngugvhkrufiqzbwy.cpp",
"spaghetti/krybwrwfstxaezwxmkayhjmxtcvautovmxjgekpnwwombilhio.cpp",
"spaghetti/ncxtaeauimhrwcveowaealoixmrvpfkgbbjavzmalsakkxkmah.cpp",
"spaghetti/rqgklfkhnovguarsdanhtjsvomsuzxfftdfhkvichpqcrfbhmm.cpp",
"spaghetti/sgflvizqvdlyzegzrpoyulorhpbrokgiybqyuyumjljlhhwssg.cpp",
"spaghetti/ksswxhjlrlgsxihflgdrovxfnvksvssmwskwaltqdtvznduzju.cpp",
"spaghetti/qodokwsdtmzhpyfgcovbaonhafknwbbsopaqlskrttxwfzldhq.cpp",
"spaghetti/ldffqiblesgnctgxlpdrpmbeodlqfnuapouqjhlcqdmmsfdtlq.cpp",
"spaghetti/sgnimoncptssuutklgtlcntgrepahzprjnmsvfwbzvcfnrupok.cpp",
"spaghetti/xcyayumiuivakrpelbxpnxghjzjaoctgmfimnafhdzieeceljs.cpp",
"spaghetti/qwlwszwgjuzzwkcxkdnojqvydgvkpyqatafphhnblaizycavdo.cpp",
"spaghetti/dqzauekrnzczhrmqjsrfgthksfsepxjhoeniyedjgbbgqvnsfb.cpp",
"spaghetti/ibgtlivtxmdoszzxndgryskmmiphxvohwmdmqxwvnqoaaoawjk.cpp",
"spaghetti/ygavcvzsgtgxceuyqfwmlxybdorobejnmovcmbhprnzdkduldl.cpp",
"spaghetti/uximdcrsxpfosrxlztonbwpxahwetyhkjkqmngvrxqyfrhbtrh.cpp",
"spaghetti/tmgaxrjumftbnedsdoollafrdzxnuqyiuhojzwhasmagpcaagh.cpp",
"spaghetti/uvnbesjngbewzglfykjwrvqzshjhzezepcqgaqermghknoltiz.cpp",
"spaghetti/rtfuuvbljlxzofzeomsxrustzhewnssywsopjmnjvoiphdzgls.cpp",
"spaghetti/wgtdpbvpvyvpsllcwmazycghzhzbcoelefytefapclgdpoggrn.cpp",
"spaghetti/rqbfvvvcalhqrfzwkorzjjwcumwxaygvmguazfabauwxxjxnow.cpp",
"spaghetti/mzgcfbajvgtymufrtxroiowuzbcoftanfqyuugoqlwrgbubkqe.cpp",
"spaghetti/smsohkdnzcwvsrfnkpqwmoxlvwjabsinsecaqhblginypsqsup.cpp",
"spaghetti/pifrgmpkgwrniduoaawvlhflllvlqmfgdcblmxjlrqduvubkbo.cpp",
"spaghetti/xzfjfhncahkikjalzqcnyuhhxjxuifhulamvgaqyvzhcibvasg.cpp",
"spaghetti/tkafhlaqnmyzfrgkovsiqxlthzmddfivevgvbdufpokoezbbno.cpp",
"spaghetti/uiifhqicvfsrvdlhzdingqzklrqxyvmojdbmelagiklnngyoav.cpp",
"spaghetti/yndeqskqxkcyhtbcmdbyhioiaxttxxbtriwenbsxcewrvjpdos.cpp",
"spaghetti/lrcgqhbnutkatcdmiqdfjqmhgvauqsmclftytgwrayxhicuomj.cpp",
"spaghetti/dmvmitbjinequhanfgywqsgsujftmaovpgbvsxqmdxikcvmcxr.cpp",
"spaghetti/xlxbuwvvbrgrogogauhttbolaepqegbzqxhtfsdsdvhmbcfzoh.cpp",
"spaghetti/naljewoqbdexeqdsehwhauaqobkjhmyxabkimbftwvphmfperh.cpp",
"spaghetti/oqbhqmeorgvwhqqcotvjgfynaybfsbcvcpnwcudnyguyigkkch.cpp",
"spaghetti/bfafmbskvfehctsyfoeubmfhqurjmpfcgzvvhynnbrxeiiruda.cpp",
"spaghetti/hqorbdikhrkiesjkpqdbyfazekqontcerjwvxcbljohfvjanny.cpp",
"spaghetti/qoktjshpnupifwuqkqtohcvyfsupncwdlajyjsmvqxdcoidnfp.cpp",
"spaghetti/ajgqzrmfnfvdxmdfafdmygvguaurpmsyvqdmldjyuydqcvbieg.cpp",
"spaghetti/ytlcmymtbyslsdzztpemqphobdcxqidilgkzjbhmnvunfqscvx.cpp",
"spaghetti/vetwaxjlqmgrlqoqetidkamfcgcdegmdjgaueinhbqspbrqxql.cpp",
"spaghetti/ypdiccpehzbrtiqkvtelehbfoxstjtlcsqeqgpivbgnnshjjfq.cpp",
"spaghetti/zblifiikrthfolbsbizugkwjaqzuoftmmgihkeuzrezfwxdrgl.cpp",
"spaghetti/chpdpqemeebqpcrqolkzgxonkopjspqdcfenwtdoqbayjizgzu.cpp",
"spaghetti/ljlemzvwdiiidagrftkqaofdlxfhsjuxeieaykjawryucjoatn.cpp",
"spaghetti/lugbrvtvqrhrnuooxdnrrknhobxpeadhrjtcdjabooqezdrnno.cpp",
"spaghetti/retsncxxoihfrwfvmznlzjadjjvuhbpcjmnxtodokpbdzgtfep.cpp",
"spaghetti/rmcrwbocgqntlctqejhojrhzvbdendgwlvlqngabjujylsglhp.cpp",
"spaghetti/msniqyqwudqnczwrkywxnqtvwtqmnxrgqufptcndwylbrzjxzr.cpp",
"spaghetti/oglbcurahirgekwfjtbsrbfbqdyasstlglwxrbgebcmmmdziry.cpp",
"spaghetti/tldaiebewrtiiwvspoyapucnirsukqyvwhfvswkvhetjqucpim.cpp",
"spaghetti/sztexwoxeyocvvswbgurckfiabxmendvyszjfpplhqppoikzvn.cpp",
"spaghetti/ihkgahsnhqjahoeaovosemtjtpanzuhladilwasagansldhkdy.cpp",
"spaghetti/pmlzzwdvyvwydvyizgjllsjrjccvdvhpmfxxtlrtigcrtracpr.cpp",
"spaghetti/hfskleslkaobvyxnygetzmjcslpbmtffqzcvwmmcxvbuhlvcxe.cpp",
"spaghetti/bvvwfywaffutdjeraqnbeerlnioaptyzfxfqqygvwxwueatmwr.cpp",
"spaghetti/gookrancgianttrhxcgteszwqqmenpzlufeovtglqggioabzdh.cpp",
"spaghetti/uehbpyxmbpcypivelhdojbujvanhtyccpndwxearoeamnxgzcb.cpp",
"spaghetti/gsczpvzbhaooswdchutcsmxsfaimlwfeqcxmjbpytlskxatash.cpp",
"spaghetti/lvlgxutzyamikczpcwibbcvjuxaykeonplfvldqgubuebdtzhn.cpp",
"spaghetti/tstxfhgunalmrtaqapebujxeghhgnpkihsyoswzcivwsktnpgz.cpp",
"spaghetti/yyfoppksjainlhuvvoxplvjvdzjbszphrazpefpjknjmfqscyq.cpp",
"spaghetti/sbkzigweceuduttbqivdkknsllzxliorwbsxpeqzmgxpgexsid.cpp",
"spaghetti/aguqnuqtekdwmcyocyjrhrwdqylrptwemvnamejtrckkzjvpoc.cpp",
"spaghetti/mhvnzraoouqfdklbtnxreqaehopvttktssthinivcryikrybsf.cpp",
"spaghetti/gbpescgnyvjwcjnstkafhrzjhxfbztfkqxiskoldcyfehhbcxi.cpp",
"spaghetti/wpnxifsfsmnyeuvgsmpasyhbyqkapdzyxphxtzimhxqsykmpwb.cpp",
"spaghetti/snfennmcapymvrlpnpclbgzksnveokzdwpzxfyuudcrtdfadre.cpp",
"spaghetti/yfmjekiwcxqshivjdirxtgxoifjwrgtxvcofqjbrhsiijjskej.cpp",
"spaghetti/siqemdmhhcqtpudlusyulwmalkwxegzwgxniamyeiwrgsahcax.cpp",
"spaghetti/vtiqnmyyzcpynefvdpqjmnjwhalninuzqgymbbzrnlgxquzlqv.cpp",
"spaghetti/jpsrkxielxlehdnydwqpzzltxlfclzakrexgzfoznpnddiokys.cpp",
"spaghetti/lfjdrhjmemmltbcbcttnkhcjkuamwelajyuundxtwjcvevyvqq.cpp",
"spaghetti/rsgmbkoijkypavinssrpeepnxqpyzfwtbqvewokcsravedzzpc.cpp",
"spaghetti/tdnszjrmzbjbkeobcccdpbmyamqzmtpwwqyntoyoovsoyqewic.cpp",
"spaghetti/jhxmankhwqywbmhbuxvxigpqqsifcvzsmxbjztxkrlpzsdnhdt.cpp",
"spaghetti/kllprmlvmtyhabctktipmbzqcgywkozaoripgwewaqcqjfojmg.cpp",
"spaghetti/chzvdulxylcdzixzjlrgovinsrkctbvcvwoauhmsjuycqhsrrp.cpp",
"spaghetti/pzbzstzvuswrmfqyqayfhgzkffpzyilhxlfwkzjgdvgixpdqpc.cpp",
"spaghetti/frknrkeibhkzsaiqekupdirdmwizjzlygncjqptdxpgavniwyn.cpp",
"spaghetti/xpjzpkblymgmxawatnjbzgkfromvujigstnehzpcagjtxdjfyo.cpp",
"spaghetti/gpymetgeyyiwmqtxczpaglghbxufdvrungjldlnjajvhyagkju.cpp",
"spaghetti/yxihqkmsrmscbdztlaxnzhhyvflhxjikqpnyufdzlsynqucwyk.cpp",
"spaghetti/iysgeitcdldgxnkpocrechiwciwhbbbctrkusxexermdbreztb.cpp",
"spaghetti/gxwmzhiikdukcxobwzmarpgtevotuwzwpvyjpcqsfefjzzwxrm.cpp",
"spaghetti/iaecvlqktgkbxasxhsilsasqtlcwgqnsvvuhxykdfcvdjcvczv.cpp",
"spaghetti/plfrsfbbbgjqxxlthmevilptzbdjbktcvrclxaniyvxbgiptek.cpp",
"spaghetti/slkujtdknpyndridmpwcgbvxuawscfrljstfwvpmzxycfpbpvq.cpp",
"spaghetti/cbznfaqlcsxcunadomamqfwspjhsesjzpoxxbnoejxdwjfnecj.cpp",
"spaghetti/dhokpbpcvzqlsolslehczhyqudugoqczubzjshwlrvsmnnsbji.cpp",
"spaghetti/tcjbyqgtoylnpctxlgbcysapjpvqllgwzureosicdambypdocy.cpp",
"spaghetti/qxecmpoitqtpdyeumdbdfdyidxnbndzrnlviojinuqyxyglucp.cpp",
"spaghetti/nebwpbpbsokfblfcdoqptvnlakmjhnclhnqqplrsslbcomoxff.cpp",
"spaghetti/khgyjkyieeaomicojuzkewykloeooejjcauiubrljhpjiqrhjy.cpp",
"spaghetti/psotqgfoicptyfqggfkwhkjwyaqvmzmnbqjohnzwmghjnaxfve.cpp",
"spaghetti/znxmlwbedrctssyajamboadihyziwjpezyglhemygmjesdiycp.cpp",
"spaghetti/ekvebarjreidkaxcssntrzdwhvtzlfjgjszsoorotnrlrncqoa.cpp",
"spaghetti/fmcsuuahfryuftpsmdmyfttnnftyqjizlshaurgjlobhdxnlyi.cpp",
"spaghetti/nkkdzjjfvwopooqnlcivscopgvvyjvoixfpzpyajtwlxmszbcz.cpp",
"spaghetti/ayvgnofqweiesllskmpithbwgpzuekbthcbzmwuwfgbszwyscz.cpp",
"spaghetti/djoodumzqpuejednbfofcqohalvroroxsdeqpjtzywxopvodhx.cpp",
"spaghetti/gitqhgznnkvhcvwonsbljbwzfryfdjwrveupckassrafhuqudw.cpp",
"spaghetti/oqdoesjogfnmyorloreqdtljzzfaofqfexbqyhiishvujfmqbx.cpp",
"spaghetti/zzibjedgygsdnzkclvzmqyfqvaqozqpnutrefnlgmqvcmimlha.cpp",
"spaghetti/utvmyapvbtlkdnhqtdquzzfhcvylqifvbpnnkihdjxibxlqalw.cpp",
"spaghetti/ysdhhqwvzmrgwlgzoomxnbhofswnshmaxtivntzyhglvcwgfsn.cpp",
"spaghetti/tzcyzmfzgpwlmmwzjyztyedvtjwnafjcoebiqpllbkcgqrtlku.cpp",
"spaghetti/odpeswpyfiutfonuaxezaffpnvcsiualbyjpszbatalvtztiwu.cpp",
"spaghetti/gjzmlkoxjnastqhmykroyvvycsvujbspjbojqyydkfampwrujw.cpp",
"spaghetti/xhfvwsawrgulvmvkkxnjknpngavtbmikgmbmlbdtekqcioyyey.cpp"]
for fstr in files:
    fileobj=open(fstr,mode='rb')
    data=fileobj.read()
    fileobj.close()
    print(str(data)[2:-1],end='')
```

修饰代码，直接输出：

```c++
#include <iostream>
using namespace std;
int main() {
    string _ = "Code that overuses }{ GOTO statements ratherzx than_structured programminjg constructqs, resulting in convoluted and unmaintainable programs, is often called spaghetti code. Such code has a complex and tangled control structure, resulting in a program flow that is conceptually like a bowl of spaghetti, twisted and tangled.";  
    cout << "People always say that my code is spaghetti, but I don\'t see it. Can you help me find the flag?"  << endl;
    string ____;
    cin >> ____;
    string __ = "";
    for ( int ______ = 0;______ < 55;++______) {
        __ += "a";
    }
    __[ 0 ] = _[ 63 ];
    __[ 1 ] = _[ 71 ];
    __[ 2 ] = _[ 34 ];
    __[ 3 ] = _[ 66 ];
    __[ 4 ] = _[ 20 ];
    __[ 5 ] = _[ 71 ];
    __[ 6 ] = _[ 5 ];
    __[ 7 ] = _[ 51 ];
    __[ 8 ] = _[ 71 ];
    __[ 9 ] = _[ 15 ];
    __[ 10 ] = _[ 51 ];
    __[ 11 ] = _[ 128 ];
    __[ 12 ] = _[ 7 ];
    __[ 13 ] = _[ 2 ];
    __[ 14 ] = _[ 51 ];
    __[ 15 ] = _[ 255 ];
    __[ 16 ] = _[ 6 ];
    __[ 17 ] = _[ 3 ];
    __[ 18 ] = _[ 34 ];
    __[ 19 ] = _[ 51 ];
    __[ 20 ] = _[ 56 ];
    __[ 21 ] = _[ 1 ];
    __[ 22 ] = _[ 2 ];
    __[ 23 ] = _[ 3 ];
    __[ 24 ] = _[ 51 ];
    __[ 25 ] = _[ 71 ];
    __[ 26 ] = _[ 15 ];
    __[ 27 ] = _[ 51 ];
    __[ 28 ] = _[ 3 ];
    __[ 29 ] = _[ 7 ];
    __[ 30 ] = _[ 15 ];
    __[ 31 ] = _[ 71 ];
    __[ 32 ] = _[ 3 ];
    __[ 33 ] = _[ 13 ];
    __[ 34 ] = _[ 51 ];
    __[ 35 ] = _[ 5 ];
    __[ 36 ] = _[ 1 ];
    __[ 37 ] = _[ 51 ];
    __[ 38 ] = _[ 13 ];
    __[ 39 ] = _[ 3 ];
    __[ 40 ] = _[ 7 ];
    __[ 41 ] = _[ 2 ];
    __[ 42 ] = _[ 51 ];
    __[ 43 ] = _[ 71 ];
    __[ 44 ] = _[ 34 ];
    __[ 45 ] = _[ 51 ];
    __[ 46 ] = _[ 7 ];
    __[ 47 ] = _[ 15 ];
    __[ 48 ] = _[ 15 ];
    __[ 49 ] = _[ 3 ];
    __[ 50 ] = _[ 32 ];
    __[ 51 ] = _[ 128 ];
    __[ 52 ] = _[ 93 ];
    __[ 53 ] = _[ 276 ];
    __[ 54 ] = _[ 19 ];
    cout<<__<<endl;
    if ( ____ == __ ) {
        cout << "Congratulations, you have untangled this spaghetti!"  << endl;
    }
    else {
        cout << "Not this time!"  << endl;
    }
}
```

## ziggarettes

阅读题，照着找就行。

```c
void __noreturn main_func()
{
  __int64 v0; // r14
  _QWORD *v1; // rax
  __int64 v2; // r12
  __int64 v3; // rbp
  _QWORD *v5; // rax
  _QWORD *v6; // r15
  _QWORD *v7; // r13
  __int64 v8; // rcx
  __int64 v9; // rax
  _QWORD *v10; // rdx
  _QWORD *v11; // rsi
  _QWORD *v12; // rcx
  bool v13; // cf
  unsigned __int64 v14; // rsi
  unsigned __int64 v15; // rax
  __int64 v16; // rcx
  __int64 v17; // rdi
  __int64 v18; // r8
  unsigned __int64 v19; // rcx
  char *v20; // rbx
  __int64 v21; // r12
  unsigned __int64 v22; // rax
  __int64 v23; // rax
  int v24; // r14d
  unsigned __int64 *v25; // rdx
  signed __int64 v26; // rax
  rlim64_t *v27; // r15
  __int64 v28; // r9
  rlim64_t rlim_max; // rcx
  signed __int64 v30; // rax
  __int16 v31; // ax
  __int16 v32; // ax
  __int64 v33; // r9
  unsigned __int64 v34; // r10
  char *v35; // rsi
  size_t v36; // rdx
  unsigned __int64 v37; // rax
  __int16 v38; // r8
  __int64 v39; // r10
  int v40; // ecx
  unsigned __int64 i; // rax
  char v42; // cl
  __int64 v43; // rax
  __int64 v44; // rbx
  __int64 v45; // r14
  int j; // edi
  signed __int64 v47; // rax
  __int64 v48; // rdx
  const char *v49; // rsi
  unsigned int v50; // [rsp+0h] [rbp-78h] BYREF
  int v51; // [rsp+8h] [rbp-70h] BYREF
  __int64 v52; // [rsp+10h] [rbp-68h]
  _QWORD *v53; // [rsp+18h] [rbp-60h]
  struct rlimit64 old_rlim; // [rsp+20h] [rbp-58h] BYREF

  v0 = *(_QWORD *)qword_204000;
  v1 = (_QWORD *)(qword_204000 + 8LL * *(_QWORD *)qword_204000 + 16);
  v2 = qword_204000 + 8;
  v3 = -1LL;
  v53 = v1;
  do
    ++v3;
  while ( *v1++ != 0LL );
  qword_204008 = (__int64)v1;
  v5 = v1 + 1;
  v6 = 0LL;
  v7 = 0LL;
  while ( 1 )
  {
    v8 = *(v5 - 1);
    switch ( v8 )
    {
      case 3LL:
        v6 = (_QWORD *)*v5;
        break;
      case 5LL:
        v7 = (_QWORD *)*v5;
        break;
      case 0LL:
        v9 = 0LL;
        v10 = v7;
        v11 = v6;
        v12 = 0LL;
        while ( 1 )
        {
          v13 = v10 == 0LL;
          v10 = (_QWORD *)((char *)v10 - 1);
          if ( v13 )
            break;
          if ( *(_DWORD *)v11 == 6 )
          {
            v9 = (__int64)v6 - v11[2];
          }
          else if ( *(_DWORD *)v11 == 7 )
          {
            v12 = v11;
          }
          v11 += 7;
        }
        if ( v12 )
        {
          v15 = v12[2] + v9;
          v14 = v12[6];
          v17 = v12[4];
          v16 = v12[5] - 1LL;
        }
        else
        {
          v14 = 8LL;
          v15 = 0xAAAAAAAAAAAAAAAALL;
          v16 = -1LL;
          v17 = 0LL;
        }
        v18 = (v14 + v16) & -(__int64)v14;
        v19 = (v18 + 23) & 0xFFFFFFFFFFFFFFF8LL;
        qword_204030 = v15;
        qword_204038 = v17;
        qword_204040 = v19 + 16;
        qword_204048 = v14;
        qword_204050 = v18;
        qword_204058 = v19;
        if ( v14 > 0x1000 || (v20 = (char *)&unk_205000, v19 >= 0x20F1) )
        {
          v22 = sys_mmap(0LL, v19 + 16 + v14 - 1, 3uLL, 0x22uLL, 0xFFFFFFFFFFFFFFFFLL, 0LL);
          if ( v22 >= 0xFFFFFFFFFFFFF001LL )
            v22 = sub_202C4B();
          v52 = v2;
          v21 = v0;
          v20 = (char *)((qword_204048 + v22 - 1) & -qword_204048);
        }
        else
        {
          v52 = qword_204000 + 8;
          v21 = v0;
        }
        sub_202F7B(v20, 0LL);
        v23 = qword_204058;
        *(_QWORD *)&v20[qword_204058] = 1LL;
        *(_QWORD *)&v20[v23 + 8] = v20;
        v24 = (_DWORD)v20 + qword_204050;
        *(_QWORD *)&v20[qword_204050] = &v20[qword_204050];
        sub_202F5B(v20, qword_204030, qword_204038);
        v26 = sys_arch_prctl((struct task_struct *)0x1002, v24, v25);
        v27 = v6 + 5;
        v28 = v52;
        while ( 1 )
        {
          v13 = v7 == 0LL;
          v7 = (_QWORD *)((char *)v7 - 1);
          if ( v13 )
            goto LABEL_35;
          if ( *((_DWORD *)v27 - 10) == 1685382481 )
            break;
          v27 += 7;
        }
        if ( (unsigned __int64)sys_prlimit64(0, 3u, 0LL, &old_rlim) < 0xFFFFFFFFFFFFF001LL )
        {
          rlim_max = *v27;
          if ( *v27 >= old_rlim.rlim_max )
            rlim_max = old_rlim.rlim_max;
          if ( rlim_max > old_rlim.rlim_cur )
          {
            old_rlim.rlim_cur = rlim_max;
            v30 = sys_prlimit64(0, 3u, &old_rlim, 0LL);
          }
        }
LABEL_35:
        qword_204010 = v28;
        qword_204018 = v21;
        qword_204020 = (__int64)v53;
        qword_204028 = v3;
        v31 = sub_20269A(13LL, &off_2003F0);
        if ( v31 )
        {
          old_rlim = (struct rlimit64)xmmword_2006C8[v31];
          sub_202CC2();
        }
        v50 = 1;
        v32 = sub_202714(&v50, (__int64)"Do you know the flag?\n", 22LL);
        if ( !v32 )
        {
          v33 = 35LL;
          v34 = 0LL;
          while ( 2 )
          {
            if ( v34 > 0x22 )
            {
LABEL_45:
              for ( i = 0LL; i != 35; ++i )
              {
                if ( i < 0x23 )
                {
                  v42 = *((_BYTE *)&old_rlim.rlim_cur + i);
                  switch ( i )
                  {
                    case 0uLL:
                    case 0x20uLL:
                      if ( v42 != 'p' )
                        goto LABEL_115;
                      continue;
                    case 1uLL:
                      if ( v42 != 'i' )
                        goto LABEL_115;
                      continue;
                    case 2uLL:
                      if ( v42 != 'n' )
                        goto LABEL_115;
                      continue;
                    case 3uLL:
                      if ( v42 != 'g' )
                        goto LABEL_115;
                      continue;
                    case 4uLL:
                      if ( v42 != '{' )
                        goto LABEL_115;
                      continue;
                    case 5uLL:
                      if ( v42 != 'z' )
                        goto LABEL_115;
                      continue;
                    case 6uLL:
                    case 9uLL:
                      if ( v42 != '1' )
                        goto LABEL_115;
                      continue;
                    case 7uLL:
                      if ( v42 != 'G' )
                        goto LABEL_115;
                      continue;
                    case 8uLL:
                    case 0xBuLL:
                    case 0x10uLL:
                    case 0x15uLL:
                      if ( v42 != '_' )
                        goto LABEL_115;
                      continue;
                    case 0xAuLL:
                      if ( v42 != 'S' )
                        goto LABEL_115;
                      continue;
                    case 0xCuLL:
                      if ( v42 != 'v' )
                        goto LABEL_115;
                      continue;
                    case 0xDuLL:
                    case 0x17uLL:
                      if ( v42 != '3' )
                        goto LABEL_115;
                      continue;
                    case 0xEuLL:
                      if ( v42 != 'R' )
                        goto LABEL_115;
                      continue;
                    case 0xFuLL:
                      if ( v42 != 'Y' )
                        goto LABEL_115;
                      continue;
                    case 0x11uLL:
                      if ( v42 != 'C' )
                        goto LABEL_115;
                      continue;
                    case 0x12uLL:
                      if ( v42 != '0' )
                        goto LABEL_115;
                      continue;
                    case 0x13uLL:
                    case 0x1EuLL:
                      if ( v42 != 'O' )
                        goto LABEL_115;
                      continue;
                    case 0x14uLL:
                    case 0x21uLL:
                      if ( v42 != 'l' )
                        goto LABEL_115;
                      continue;
                    case 0x16uLL:
                    case 0x1FuLL:
                      if ( v42 != '2' )
                        goto LABEL_115;
                      continue;
                    case 0x18uLL:
                      if ( v42 != '4' )
                        goto LABEL_115;
                      continue;
                    case 0x19uLL:
                      if ( v42 == 'm' )
                        continue;
                      goto LABEL_115;
                    case 0x1AuLL:
                    case 0x1CuLL:
                      if ( v42 != 'K' )
                        goto LABEL_115;
                      continue;
                    case 0x1BuLL:
                    case 0x1DuLL:
                      if ( v42 != 'I' )
                        goto LABEL_115;
                      continue;
                    case 0x22uLL:
                      if ( v42 == '}' )
                        continue;
LABEL_115:
                      v50 = 1;
                      v48 = 7LL;
                      v49 = "Wrong!\n";
                      break;
                  }
                  goto LABEL_116;
                }
              }
              goto LABEL_114;
            }
            v35 = (char *)&old_rlim + v34;
            v36 = v33 - v34;
LABEL_41:
            v37 = sys_read(0, v35, v36);
            v40 = -(int)v37;
            if ( v37 < 0xFFFFFFFFFFFFF001LL )
              LOWORD(v40) = v38;
            switch ( (__int16)v40 )
            {
              case 0:
                v34 = v37 + v39;
                if ( !v37 )
                  goto LABEL_45;
                continue;
              case 1:
              case 2:
              case 3:
              case 6:
              case 7:
              case 8:
              case 10:
                goto LABEL_108;
              case 4:
                goto LABEL_41;
              case 5:
                v32 = 3;
                goto LABEL_109;
              case 9:
                v32 = 18;
                goto LABEL_109;
              case 11:
                v32 = 13;
                goto LABEL_109;
              case 12:
                goto LABEL_105;
              default:
                switch ( (unsigned __int16)v40 )
                {
                  case 0x15u:
                    v32 = 16;
                    break;
                  case 0x68u:
                    v32 = 14;
                    break;
                  case 0x69u:
LABEL_105:
                    v32 = 9;
                    break;
                  case 0x6Eu:
                    v32 = 17;
                    break;
                  default:
LABEL_108:
                    v32 = 15;
                    break;
                }
                break;
            }
            break;
          }
        }
        while ( 1 )
        {
LABEL_109:
          v43 = v32;
          v44 = *(_QWORD *)&xmmword_2006C8[v43];
          v45 = *(_QWORD *)(v43 * 16 + 2098896);
          v51 = 2;
          sub_20284A(&unk_207104);
          v50 = 2;
          if ( !sub_202714(&v50, (__int64)"error: {s}\n", 7LL)
            && !(unsigned __int16)sub_20291A(v44, v45, &unk_2006A0, &v51) )
          {
            LODWORD(old_rlim.rlim_cur) = 2;
            sub_202714((unsigned int *)&old_rlim, 2100287LL, 1LL);
          }
          sub_202888(&unk_207104);
          for ( j = 1; ; j = 0 )
          {
            v47 = sys_exit_group(j);
LABEL_114:
            v50 = 1;
            v48 = 9LL;
            v49 = "Correct!\n";
LABEL_116:
            v32 = sub_202714(&v50, (__int64)v49, v48);
            if ( v32 )
              break;
          }
        }
    }
    v5 += 2;
  }
}
//ping{z1G_1S_v3RY_C0Ol_234mKIKIO2pl}
```

