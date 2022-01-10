#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def electricityExperiment(self, row: int, col: int, position: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        def make_unit():
            mat = [[0] * row for _ in range(row)]
            for i in range(row):
                if i > 0:
                    mat[i][i - 1] = 1
                mat[i][i] = 1
                if (i + 1) < row:
                    mat[i][i + 1] = 1
            return mat

        def mat_mul(a, b):
            R, K, C = len(a), len(a[0]), len(b[0])
            res = [[0] * C for _ in range(R)]
            for k in range(K):
                for i in range(R):
                    for j in range(C):
                        res[i][j] += (a[i][k] * b[k][j]) % MOD
                        res[i][j] %= MOD
            return res

        cache = [None] * 32
        cache[0] = make_unit()
        for i in range(1, len(cache)):
            cache[i] = mat_mul(cache[i - 1], cache[i - 1])

        def solve(r0, r1, step):
            b = [[0] * 1 for _ in range(row)]
            b[r0][0] = 1
            for i in range(32):
                if (step >> i) & 0x1:
                    b = mat_mul(cache[i], b)
            return b[r1][0]

        position = [(r, c) for (r, c) in position]
        position.sort(key=lambda x: x[1])
        ans = 1
        for i in range(1, len(position)):
            r0, c0 = position[i - 1]
            r1, c1 = position[i]
            res = solve(r0, r1, c1 - c0)
            ans = (ans * res) % MOD
            if ans == 0:
                break
        return ans


true, false, null = True, False, None
cases = [
    (5, 6, [[1, 3], [3, 2], [4, 1]], 0),
    (3, 4, [[0, 3], [2, 0]], 3),
    (5, 6, [[1, 3], [3, 5], [2, 0]], 6),
    (20,
     1000000000,
     [[12, 23017283], [5, 665033307], [5, 147145651], [1, 416801369], [0, 113559737], [1, 957928463], [6, 587013299],
      [18, 89512712], [6, 810827361], [8, 269343331], [8, 100534258], [8, 411842458], [2, 974905020], [13, 718501958],
      [18, 480330856], [14, 441534303], [14, 151284255], [0, 906612589], [5, 536318286], [15, 311094459],
      [18, 356914235], [5, 977246335], [15, 133544717], [18, 708758176], [9, 442071998], [3, 500810969],
      [10, 141956570], [8, 404352716], [15, 398487591], [16, 327771819], [7, 973892197], [0, 788494532],
      [12, 353390486], [15, 71740681], [12, 544910004], [3, 50924645], [8, 454520533], [16, 504383502], [4, 18141365],
      [9, 396311777], [11, 466748711], [5, 305792190], [18, 438508913], [14, 406505052], [16, 54743102],
      [12, 972477447], [12, 219518458], [15, 625287554], [19, 233585792], [2, 434439586], [4, 470243257],
      [15, 271356057], [13, 15074385], [17, 246055667], [10, 345916744], [4, 442060297], [14, 152077800],
      [19, 511764781], [3, 636869038], [10, 743797838], [15, 3690988], [0, 615521783], [14, 260649962], [1, 810223203],
      [14, 366159704], [4, 652187387], [17, 302714789], [0, 216973730], [19, 343590729], [0, 611576053],
      [10, 789888605], [2, 595265450], [7, 3285255], [15, 56262325], [6, 136720717], [7, 631083204], [2, 949221067],
      [12, 76360707], [7, 451326785], [7, 889402779], [8, 115625486], [7, 206117268], [16, 396989375], [15, 494537993],
      [16, 78293863], [3, 855019509], [0, 5987069], [3, 353144601], [6, 475620638], [10, 860813338], [4, 773670889],
      [12, 570758098], [16, 932663538], [10, 249730136], [15, 553101245], [11, 70997617], [14, 493568874],
      [17, 526071235], [2, 580292318], [6, 486154537], [5, 411497335], [4, 663391742], [7, 3550273], [15, 204711797],
      [3, 375511053], [2, 583901130], [3, 292816265], [15, 847849700], [1, 288424657], [9, 34031992], [19, 585981618],
      [1, 594610869], [1, 587265784], [3, 465462462], [18, 468059769], [1, 240890406], [12, 816381416], [9, 628845223],
      [7, 425912845], [13, 321015263], [8, 18038795], [18, 643548237], [19, 164472708], [16, 219437426], [0, 198036292],
      [2, 921287410], [16, 619032534], [17, 233182546], [8, 977509284], [3, 3583054], [15, 117321004], [1, 598875542],
      [8, 833060287], [14, 849591199], [17, 137632412], [14, 528475344], [12, 704356231], [0, 872597934],
      [11, 502826387], [4, 424014838], [11, 458526957], [5, 935841457], [11, 256656663], [16, 186885233],
      [16, 555591104], [17, 290906897], [6, 893145453], [16, 660204197], [15, 139191163], [5, 787570720],
      [18, 988449659], [13, 501939827], [5, 921483459], [4, 284409483], [14, 894719155], [7, 475080174], [5, 780683481],
      [15, 714795063], [6, 190279059], [1, 718752446], [0, 452575333], [17, 747020263], [1, 106561558], [0, 246520388],
      [17, 722503002], [3, 813883616], [17, 401877840], [19, 792298185], [0, 251066738], [8, 284115608], [6, 427142475],
      [16, 897874880], [3, 53035058], [1, 991387770], [16, 599559558], [5, 319436250], [16, 289589337], [18, 288378300],
      [7, 668019295], [4, 238330923], [14, 865980750], [10, 241451100], [12, 818814124], [1, 246339198], [4, 884479088],
      [14, 456769070], [6, 691248586], [18, 137697433], [4, 404259416], [17, 602137325], [0, 754802775], [5, 607068750],
      [19, 708990709], [7, 643138300], [15, 478026333], [0, 188103296], [12, 964144736], [9, 641657100], [6, 922474362],
      [2, 503686902], [4, 268007586], [2, 159428335], [4, 137549283], [3, 609025657], [0, 165519891], [4, 647945479],
      [16, 220766707], [4, 916605110], [0, 370040268], [7, 719594446], [15, 286653855], [14, 912053290], [8, 875206784],
      [2, 94406379], [8, 123961218], [12, 631692366], [2, 150546561], [9, 82607701], [15, 263117497], [18, 280658236],
      [4, 123296349], [9, 84213905], [2, 161917773], [19, 552208881], [19, 254785780], [6, 337330521], [3, 695138244],
      [10, 882852452], [6, 155827185], [10, 731502679], [8, 18559290], [0, 961573343], [3, 422128150], [2, 503806164],
      [13, 687003958], [0, 320595156], [2, 914576993], [7, 236368790], [9, 505934039], [9, 957256731], [1, 383109900],
      [5, 94228987], [1, 766031019], [8, 734662519], [9, 899103919], [17, 704535049], [11, 227084043], [8, 286114760],
      [7, 938158662], [3, 69239103], [17, 823650527], [12, 34209782], [14, 29547670], [0, 80642062], [9, 45620614],
      [7, 969108357], [4, 626056203], [2, 510462314], [3, 225086005], [0, 543997088], [17, 686215742], [14, 512993230],
      [13, 421725268], [7, 901400735], [7, 646105410], [7, 469560958], [7, 73707995], [19, 490281994], [16, 879973450],
      [1, 560623325], [0, 835887789], [14, 573036036], [8, 638558445], [2, 957810210], [10, 322059533], [15, 212162343],
      [18, 840210871], [14, 339265925], [13, 330459564], [10, 609720910], [15, 765032845], [6, 800488274],
      [8, 117800608], [10, 593515628], [5, 451371888], [19, 666186191], [8, 632497142], [10, 597318332],
      [17, 653845081], [2, 455253022], [18, 199905848], [14, 46005850], [5, 227002280], [14, 336927331],
      [11, 302397323], [11, 994321768], [5, 935771997], [14, 88397342], [0, 453150025], [6, 759246493], [4, 615119214],
      [15, 467018219], [14, 468913211], [1, 732804054], [5, 155888471], [12, 119213640], [19, 988110076],
      [15, 614146332], [19, 290278938], [17, 457548964], [14, 97331955], [3, 902397498], [18, 217079086],
      [7, 775846257], [19, 905983884], [16, 741603058], [1, 897810870], [2, 416371208], [4, 351775236], [15, 690077153],
      [19, 399975832], [13, 939929085], [9, 847986419], [17, 339765143], [16, 107228695], [10, 347138038],
      [10, 478762311], [14, 108311002], [1, 823392794], [18, 245016295], [10, 78309629], [16, 925757772],
      [12, 973736716], [11, 574506974], [5, 758496514], [5, 34150471], [9, 413274973], [8, 599985683], [8, 821514805],
      [19, 524746737], [17, 456588157], [12, 458606407], [5, 723865646], [3, 179304745], [9, 714011357],
      [17, 456378109], [2, 604888333], [17, 688248820], [13, 241942287], [13, 826860306], [19, 273976596],
      [8, 145542603], [12, 292202237], [2, 912057557], [11, 634475358], [0, 68201889], [1, 192472276], [6, 364302685],
      [6, 797641391], [5, 5214090], [10, 434682394], [6, 473880247], [10, 437751127], [13, 845933848], [10, 774724842],
      [16, 729308073], [5, 76866665], [14, 82929134], [15, 532593175], [9, 650996712], [11, 297007712], [8, 894234907],
      [8, 786761331], [16, 549578082], [11, 330887359], [16, 362881627], [14, 933085150], [9, 461199035],
      [2, 301120413], [3, 714495313], [4, 719531272], [19, 178623363], [7, 136828015], [1, 546850163], [19, 149726501],
      [12, 549168207], [18, 916087084], [4, 350304127], [13, 21970357], [0, 323905614], [13, 255599548], [6, 22796927],
      [15, 692368830], [4, 330091023], [17, 679552318], [13, 396507910], [9, 873805702], [6, 333661815], [5, 543400681],
      [5, 339655876], [0, 39821428], [5, 458398577], [1, 206783424], [11, 988803885], [11, 664935616], [6, 360527767],
      [5, 751425779], [13, 448331059], [13, 572859167], [1, 503022573], [10, 759345769], [9, 791816857], [18, 30253876],
      [0, 930382663], [4, 816298183], [11, 381460917], [16, 952658690], [9, 216155393], [0, 312520988], [13, 532972272],
      [11, 804033597], [5, 481128174], [8, 818524594], [0, 278340565], [12, 96110039], [16, 267351201], [12, 353459173],
      [14, 637915640], [4, 336314050], [0, 365601437], [10, 145926079], [6, 529135437], [8, 535888332], [0, 162316050],
      [15, 186995567], [1, 74095421], [4, 475397877], [5, 878486705], [12, 922885511], [9, 794467359], [1, 2500524],
      [11, 706630437], [10, 197924116], [1, 125398916], [17, 688695956], [16, 308362228], [18, 149272603],
      [10, 350529068], [13, 311145750], [17, 487470118], [5, 167350016], [9, 69671252], [12, 258833059],
      [19, 338606749], [6, 457205845], [0, 958186286], [15, 963822973], [7, 3585819], [12, 181273809], [10, 285736728],
      [6, 121179480], [14, 405626546], [13, 824740388], [6, 260609140], [7, 821159947], [15, 519336088],
      [14, 219329208], [7, 49306498], [5, 942725261], [6, 219924946], [5, 294827372], [10, 220636951], [12, 577466473],
      [18, 842601215], [2, 284700745], [6, 511381031], [2, 787174052], [9, 682300531], [17, 925191048], [3, 2389709],
      [8, 920158448], [3, 978363231], [15, 542400524], [19, 154441585], [13, 368612769], [9, 105508045], [6, 649767438],
      [13, 496226516], [14, 952019321], [1, 518834378], [1, 258166355], [6, 413659757], [13, 579807650], [6, 527839769],
      [8, 923379697], [0, 715684654], [14, 816902076], [3, 227839457], [19, 176516468], [9, 189887075], [14, 818090754],
      [1, 193871141], [15, 975714106], [12, 74661100], [10, 785721147], [11, 54332363], [14, 952557032],
      [18, 688060734], [18, 723066479], [7, 54124076], [1, 353159026], [12, 329679623], [8, 386464402], [14, 472435744],
      [5, 23482263], [4, 261566861], [19, 250897111], [11, 784882205], [19, 904023839], [10, 304427743], [17, 80195708],
      [8, 908961723], [13, 596539141], [12, 402968459], [18, 74434901], [14, 756194200], [4, 707254605],
      [11, 597977028], [9, 614373679], [9, 403870767], [6, 734468544], [15, 168472701], [5, 636386176], [6, 986601695],
      [11, 592263367], [18, 913917889], [2, 139586666], [7, 367048283], [14, 5362120], [5, 64408889], [12, 263204692],
      [11, 292237075], [15, 75693210], [15, 759449547], [14, 483992022], [14, 335447256], [14, 328576209],
      [1, 457504360], [1, 288515629], [4, 302114127], [6, 204549471], [18, 161510157], [1, 70444782], [2, 93414847],
      [1, 376332124], [3, 482461557], [5, 503544651], [2, 390750874], [14, 672557769], [12, 307911872], [9, 147011228],
      [3, 528971085], [1, 590131312], [12, 245761023], [2, 813801624], [12, 755233300], [0, 324508441], [1, 561333323],
      [19, 930561316], [7, 720852809], [17, 610096690], [14, 881202985], [14, 970885441], [5, 394356761],
      [13, 807018076], [18, 667751233], [13, 597174680], [14, 344435610], [3, 750010844], [13, 495153198],
      [0, 757783963], [17, 35624678], [3, 130040868], [7, 147540913], [2, 803224400], [19, 138980414], [3, 285330812],
      [12, 275020330], [8, 322821380], [18, 310743504], [17, 106576515], [10, 526079401], [4, 976707879], [1, 74323882],
      [6, 126184473], [5, 963819572], [4, 507485699], [10, 117556597], [5, 220656134], [18, 835751836], [3, 350542111],
      [10, 667138554], [6, 21914404], [4, 652341230], [2, 709702758], [13, 252322375], [19, 927599158], [8, 951582550],
      [13, 749916241], [3, 716763010], [3, 361238644], [9, 907596440], [1, 718700978], [14, 596092457], [1, 324903195],
      [13, 593817591], [13, 258423545], [10, 101064935], [10, 543965567], [1, 764793063], [1, 283408120],
      [4, 542889631], [11, 637719230], [0, 471607050], [9, 790309670], [12, 642985143], [1, 259088928], [7, 582269892],
      [3, 432287205], [14, 113814929], [18, 730304167], [11, 281243839], [17, 409424455], [5, 599951134],
      [14, 731306689], [13, 905098358], [5, 496918727], [11, 674875613], [15, 447029091], [4, 382371909],
      [12, 365614705], [4, 495718681], [3, 680946690], [10, 868767186], [9, 508782607], [16, 675108588], [4, 54301150],
      [0, 977443651], [15, 917002250], [6, 116355376], [1, 825176710], [14, 841881773], [0, 882299900], [14, 672636913],
      [3, 237639197], [3, 503757173], [6, 69957888], [15, 75413895], [0, 681820297], [10, 931077789], [14, 299401190],
      [14, 905336709], [5, 764990776], [8, 817251722], [8, 738691208], [6, 718835102], [0, 691379375], [12, 778935026],
      [11, 82857795], [13, 656190798], [18, 400475248], [12, 730820722], [1, 137653222], [5, 949533920],
      [10, 528437506], [15, 82480071], [17, 166403141], [12, 51014095], [12, 245052158], [0, 92177271], [16, 709022940],
      [5, 454759119], [0, 827648510], [1, 552428106], [13, 695261081], [0, 394105840], [13, 430433794], [13, 973264388],
      [1, 405555219], [1, 835628613], [0, 681104797], [5, 585698798], [1, 194846226], [7, 791639056], [10, 979133034],
      [18, 123735800], [1, 519974335], [16, 441575491], [17, 873990978], [11, 933057531], [12, 930515313],
      [18, 902471908], [10, 915221018], [8, 817296038], [18, 60446028], [0, 473874921], [0, 810772009], [13, 824568595],
      [8, 466604393], [13, 510453656], [9, 543875686], [5, 210724832], [8, 674018754], [9, 16947658], [17, 724336207],
      [16, 492833162], [13, 402768929], [11, 297621594], [11, 943403910], [0, 595982534], [16, 762852938],
      [19, 987269928], [6, 882249825], [7, 210140208], [8, 669221400], [12, 161723803], [12, 915909855],
      [15, 822756006], [12, 150250088], [17, 474688129], [4, 751696210], [12, 525438579], [14, 434850942],
      [9, 654596779], [16, 891420591], [9, 573563726], [14, 656601999], [4, 987693546], [2, 210563456], [4, 340561970],
      [14, 931923491], [7, 8362411], [13, 754077997], [10, 276182631], [3, 490317125], [1, 799511342], [18, 790107398],
      [11, 390128950], [12, 927086024], [17, 129092059], [2, 998792772], [15, 996456280], [10, 505151666],
      [11, 527177495], [1, 157704524], [14, 535189513], [6, 653508255], [15, 170782601], [5, 654588210],
      [18, 113920608], [7, 113961758], [5, 19078723], [17, 63799371], [7, 442544795], [10, 186814996], [1, 989381750],
      [9, 415684132], [12, 574666082], [6, 664620458], [9, 156350389], [6, 586441045], [0, 343380574], [2, 410070483],
      [13, 957819418], [19, 265308870], [8, 923601964], [11, 992079941], [14, 905478737], [19, 90753235],
      [9, 896736754], [4, 64991683], [12, 868295829], [4, 614847057], [9, 867550948], [4, 701010383], [14, 401537157],
      [0, 136297929], [11, 428480826], [9, 356770420], [14, 689375932], [1, 829912507], [19, 319163816], [0, 908142934],
      [18, 146983831], [18, 784753884], [7, 929992113], [9, 717192491], [5, 591223064], [9, 725572707], [6, 120926632],
      [11, 6194353], [13, 274426040], [2, 317562483], [7, 701463214], [0, 999659600], [19, 559944577], [2, 181271262],
      [18, 715615207], [4, 413058000], [17, 5903880], [10, 144967842], [17, 832042048], [2, 375643451], [10, 883187392],
      [12, 523895546], [2, 379669247], [14, 171529709], [17, 386873264], [10, 944582371], [4, 867590696],
      [7, 771627788], [8, 766034315], [2, 179932227], [10, 330272013], [14, 222181348], [18, 585832917], [5, 620825674],
      [5, 452215321], [11, 593431886], [7, 887605653], [11, 470600512], [0, 938080653], [19, 834939115], [1, 146724527],
      [12, 989457564], [9, 756596378], [7, 558012575], [8, 332191620], [0, 772726642], [6, 294191644], [3, 397348381],
      [9, 122152580], [9, 506635328], [7, 17917798], [0, 485087366], [17, 451759441], [2, 861571682], [18, 729373367],
      [13, 908522631], [14, 784840972], [4, 655278751], [3, 557918775], [16, 607101087], [3, 530240583], [3, 584506661],
      [6, 156397129], [14, 263320909], [2, 746880622], [18, 280966940], [4, 642260198], [10, 901661302],
      [17, 771554989], [15, 680072752], [10, 535417763], [6, 204941302], [0, 281959120], [17, 357271843],
      [2, 859953935], [4, 481749283], [13, 987687309], [4, 815479536], [2, 875552276], [4, 834988530], [11, 745720887],
      [10, 105291032], [9, 175533539], [19, 967155279], [6, 841501537], [5, 301030034], [12, 551910356], [6, 719824235],
      [2, 411362981], [17, 408312003], [15, 925929939], [13, 409155902], [1, 138089748], [16, 836787202],
      [3, 942670728], [2, 800259132], [19, 82627512], [11, 293249554], [3, 444208439], [12, 154640416], [12, 325678462],
      [14, 166987896], [2, 753949376], [8, 743784259], [8, 194346802], [4, 735966112], [5, 927069549], [17, 691555113],
      [19, 660729192], [14, 392990765], [0, 350557894], [16, 577029647], [1, 861622296], [4, 628164139], [5, 783600965],
      [3, 607555455], [4, 122780217], [0, 452202822], [2, 220819564], [18, 462002678], [1, 552333699], [15, 535988449],
      [8, 122928806], [2, 227923930], [17, 166107308], [6, 307691187], [18, 690203111], [10, 473856195],
      [10, 742607182], [4, 481017573], [7, 701337874], [3, 526043831], [2, 2069926], [5, 749950955], [19, 508383041],
      [7, 863925531], [17, 782914557], [15, 223836936], [8, 265011586], [12, 672159677], [0, 478852466], [11, 12254148],
      [9, 290593361], [7, 714210182], [9, 786088274], [19, 240815679], [7, 979609905], [2, 465527162], [5, 316278045],
      [18, 256079063], [9, 459355705], [5, 843611727], [19, 836976768], [17, 625855122], [0, 870032325], [9, 875516114],
      [15, 772018939], [16, 837141180], [13, 407157962], [3, 757856642], [13, 915674645], [9, 672981916],
      [19, 433453829], [12, 880424351], [14, 304217356], [14, 300904245], [1, 350540826], [13, 744052788],
      [13, 90630839], [1, 295789913], [9, 713130162], [10, 267114084], [12, 542546801], [19, 757548236], [9, 259599290],
      [3, 163754621], [17, 528565412], [13, 54977338], [13, 209536877], [0, 140271485], [6, 912412593], [7, 594708687],
      [5, 673900709], [8, 35205261], [15, 540655177], [5, 248752097], [18, 100050345], [11, 322636152], [11, 886151111],
      [3, 396583831], [3, 257156640], [18, 884223967], [8, 822561972], [9, 302437335], [0, 285464833], [18, 389442199],
      [3, 954596290], [9, 613038926], [16, 942910374], [15, 618029236], [14, 141794432], [14, 912510823], [1, 57862646],
      [14, 609352281], [17, 94668152], [4, 842442935], [13, 674621941]], 10)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().electricityExperiment, cases)

if __name__ == '__main__':
    pass