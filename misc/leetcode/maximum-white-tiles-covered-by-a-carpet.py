#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:

        def work(ts):
            j = 0
            t = 0
            result = 0
            n = len(ts)

            for i in range(n):
                while j < n and (ts[j][1] - ts[i][0]) < carpetLen:
                    t += (ts[j][1] - ts[j][0] + 1)
                    j += 1

                if j < n:
                    t2 = t + max(carpetLen - (ts[j][0] - ts[i][0]), 0)
                else:
                    t2 = t
                result = max(result, t2)
                t -= (ts[i][1] - ts[i][0] + 1)
            return result

        # use different endpoint strategy
        A = [tuple(x) for x in tiles]
        A.sort(key=lambda x: x[0])
        end = A[-1][1]
        B = [(end - y, end - x) for (x, y) in reversed(A)]
        a = work(A)
        b = work(B)
        ans = max(a, b)
        return ans


true, false, null = True, False, None
cases = [
    ([[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]], 10, 9),
    ([[10, 11], [1, 1]], 2, 2),
    ([[3745, 3757], [3663, 3681], [3593, 3605], [3890, 3903], [3529, 3539], [3684, 3686], [3023, 3026], [2551, 2569],
      [3776, 3789], [3243, 3256], [3477, 3497], [2650, 2654], [2264, 2266], [2582, 2599], [2846, 2863], [2346, 2364],
      [3839, 3842], [3926, 3935], [2995, 3012], [3152, 3167], [4133, 4134], [4048, 4058], [3719, 3730], [2498, 2510],
      [2277, 2295], [4117, 4128], [3043, 3054], [3394, 3402], [3921, 3924], [3500, 3514], [2789, 2808], [3291, 3294],
      [2873, 2881], [2760, 2760], [3349, 3362], [2888, 2899], [3802, 3822], [3540, 3542], [3128, 3142], [2617, 2632],
      [3979, 3994], [2780, 2781], [3213, 3233], [3099, 3113], [3646, 3651], [3956, 3963], [2674, 2691], [3860, 3873],
      [3363, 3370], [2727, 2737], [2453, 2471], [4011, 4031], [3566, 3577], [2705, 2707], [3560, 3565], [3454, 3456],
      [3655, 3660], [4100, 4103], [2382, 2382], [4032, 4033], [2518, 2531], [2739, 2749], [3067, 3079], [4068, 4074],
      [2297, 2312], [2489, 2490], [2954, 2974], [2400, 2418], [3271, 3272], [3628, 3632], [3372, 3377], [2920, 2940],
      [3315, 3330], [3417, 3435], [4146, 4156], [2324, 2340], [2426, 2435], [2373, 2376], [3621, 3626], [2826, 2832],
      [3937, 3949], [3178, 3195], [4081, 4082], [4092, 4098], [3688, 3698]], 1638, 822),
    ([[16878, 16897], [13580, 13625], [29159, 29173], [12515, 12549], [46680, 46685], [29644, 29683], [41045, 41057],
      [39301, 39338], [32851, 32890], [32266, 32289], [39397, 39443], [39619, 39645], [39952, 39954], [21121, 21127],
      [24624, 24673], [16417, 16440], [18762, 18783], [27751, 27793], [45281, 45328], [16033, 16042], [35334, 35365],
      [27220, 27230], [29430, 29461], [14742, 14756], [34601, 34612], [15510, 15560], [23479, 23521], [18389, 18427],
      [46546, 46568], [37025, 37033], [30473, 30490], [44966, 45007], [21761, 21764], [37452, 37462], [43604, 43611],
      [31419, 31462], [13014, 13018], [12379, 12400], [33371, 33398], [24597, 24602], [25645, 25669], [43443, 43486],
      [17006, 17010], [21637, 21653], [37180, 37182], [24036, 24056], [40712, 40757], [45053, 45060], [26174, 26178],
      [28828, 28844], [27092, 27111], [22642, 22649], [47457, 47467], [20242, 20260], [44692, 44705], [31177, 31179],
      [17525, 17550], [17355, 17377], [23749, 23750], [22574, 22599], [41628, 41633], [46861, 46872], [23793, 23843],
      [24145, 24164], [31544, 31576], [26700, 26748], [32579, 32597], [30153, 30165], [47242, 47292], [39836, 39846],
      [19057, 19077], [34042, 34048], [37242, 37274], [29087, 29118], [44090, 44101], [46028, 46075], [28212, 28245],
      [16697, 16722], [33105, 33110], [38072, 38104], [47511, 47528], [26524, 26560], [36595, 36606], [13472, 13507],
      [44564, 44606], [37748, 37796], [14694, 14715], [32134, 32152], [28136, 28171], [17409, 17430], [31190, 31216],
      [47683, 47710], [27822, 27852], [40274, 40324], [22823, 22834], [42659, 42696], [33487, 33494], [41430, 41449],
      [47761, 47766], [29062, 29077], [21357, 21359], [36779, 36786], [33726, 33775], [17662, 17662], [40920, 40952],
      [20136, 20157], [46179, 46229], [27570, 27604], [14313, 14357], [12276, 12281], [48794, 48837], [28032, 28065],
      [34181, 34202], [32459, 32493], [42395, 42409], [31906, 31953], [41151, 41190], [39101, 39150], [31307, 31329],
      [23074, 23115], [40973, 41021], [13370, 13374], [11622, 11647], [22850, 22870], [37640, 37653], [20493, 20521],
      [37128, 37167], [39162, 39187], [22706, 22733], [35152, 35173], [36223, 36232], [31093, 31128], [29015, 29022],
      [17050, 17091], [43289, 43308], [43233, 43256], [13019, 13029], [47945, 47952], [23380, 23396], [32665, 32676],
      [23430, 23471], [26205, 26221], [48016, 48058], [48930, 48941], [18483, 18493], [43146, 43188], [18458, 18461],
      [24387, 24422], [26650, 26675], [49046, 49077], [28955, 28966], [14383, 14403], [24462, 24503], [36021, 36034],
      [32768, 32807], [22250, 22276], [26399, 26431], [29853, 29895], [35180, 35203], [48700, 48747], [19190, 19235],
      [24090, 24095], [45506, 45546], [34944, 34975], [43905, 43955], [30873, 30906], [11415, 11434], [26777, 26820],
      [12190, 12229], [17896, 17935], [18529, 18572], [47805, 47831], [38378, 38422], [31884, 31905], [31828, 31857],
      [38515, 38546], [25491, 25512], [32395, 32404], [48597, 48617], [21894, 21894], [23129, 23158], [31343, 31383],
      [20876, 20888], [41654, 41682], [42266, 42298], [13777, 13791], [49335, 49385], [25191, 25234], [24545, 24555],
      [25149, 25180], [45577, 45604], [44005, 44008], [43093, 43117], [16790, 16830], [23609, 23625], [35609, 35651],
      [14155, 14188], [28273, 28293], [27364, 27374], [42973, 43007], [44845, 44877], [19138, 19160], [23927, 23975],
      [47553, 47574], [35755, 35765], [20554, 20604], [11806, 11833], [16048, 16090], [46619, 46650], [46344, 46390],
      [43714, 43756], [47179, 47200], [30327, 30350], [24891, 24941], [26979, 26988], [39865, 39875], [25671, 25692],
      [48491, 48497], [18575, 18588], [37196, 37220], [40516, 40563], [37319, 37368], [39665, 39689], [15044, 15090],
      [34229, 34269], [24007, 24017], [46397, 46431], [11213, 11262], [19343, 19389], [40393, 40433], [26612, 26618],
      [19488, 19511], [32407, 32436], [13750, 13771], [23172, 23208], [36612, 36629], [48965, 48980], [12040, 12051],
      [35379, 35416], [42511, 42533], [26573, 26605], [13559, 13566], [11693, 11712], [34082, 34087], [31868, 31883],
      [36536, 36579], [38469, 38496], [11953, 11968], [49520, 49541], [32898, 32912], [17839, 17858], [40158, 40178],
      [18988, 19016], [43329, 43379], [41762, 41803], [48661, 48695], [26833, 26840], [23569, 23600], [14949, 14973],
      [14044, 14047], [47384, 47409], [38110, 38119], [49164, 49170], [42726, 42772], [22097, 22143], [24715, 24733],
      [21711, 21746], [28339, 28343], [37506, 37529], [22065, 22076], [44642, 44659], [28473, 28511], [25750, 25782],
      [44233, 44240], [18195, 18201], [18000, 18031], [46759, 46795], [47873, 47879], [26015, 26039], [38976, 39021],
      [28523, 28535], [14553, 14601], [41378, 41403], [15107, 15142], [18853, 18900], [42569, 42585], [21506, 21541],
      [14291, 14309], [35801, 35844], [45139, 45188], [39507, 39547], [43043, 43052], [48240, 48272], [41330, 41351],
      [33031, 33070], [13977, 14027], [19259, 19308], [34848, 34851], [39264, 39296], [26363, 26398], [34679, 34724],
      [22187, 22218], [41873, 41890], [30714, 30763], [16572, 16574], [41983, 42020], [30645, 30680], [49212, 49215],
      [39908, 39912], [30522, 30528], [14073, 14085], [20082, 20131], [27971, 28014], [40792, 40807], [44299, 44306],
      [21040, 21074], [28429, 28432], [49786, 49797], [35425, 35450], [22750, 22786], [32202, 32230], [20760, 20761],
      [19550, 19553], [21837, 21882], [47085, 47094], [16109, 16138], [24236, 24274], [18592, 18641], [22298, 22330],
      [35248, 35292], [30998, 31048], [41634, 41644], [22477, 22498], [36958, 36961], [43835, 43885], [28554, 28575],
      [44433, 44478], [48999, 49011], [31603, 31638], [29772, 29811], [11568, 11592], [43619, 43662], [38569, 38577],
      [39495, 39496], [48313, 48349], [25569, 25597], [42120, 42168], [25700, 25718], [18130, 18177], [14900, 14904],
      [12069, 12089], [16933, 16983], [21169, 21193], [12705, 12754], [42458, 42474], [30566, 30609], [21242, 21257],
      [20924, 20961], [21437, 21478], [11335, 11371], [40657, 40670], [14989, 15017], [20418, 20451], [12953, 12988],
      [35911, 35916], [31506, 31523], [32619, 32639], [31228, 31267], [12896, 12944], [16298, 16319], [28355, 28360],
      [24296, 24335], [35960, 35971], [34799, 34821], [38712, 38722], [12111, 12147], [27139, 27172], [43544, 43574],
      [27928, 27929], [20651, 20680], [22670, 22704], [28370, 28402], [13522, 13534], [14759, 14798], [22019, 22037],
      [47540, 47546], [46466, 46485], [30845, 30860], [12569, 12593], [37911, 37939], [19821, 19847], [45962, 45998],
      [37817, 37866], [12308, 12355], [13066, 13082], [27002, 27045], [32339, 32389], [41227, 41239], [41715, 41750],
      [41079, 41101], [45827, 45868], [44806, 44811], [37977, 38024], [29516, 29531], [21277, 21319], [36269, 36278],
      [24213, 24233], [20711, 20721], [11983, 12000], [41500, 41517], [41923, 41954], [29555, 29589], [35466, 35487],
      [33197, 33217], [24371, 24374], [11436, 11457], [33074, 33074], [45700, 45742], [25433, 25476], [48400, 48440],
      [35698, 35706], [17692, 17720], [29605, 29608], [20012, 20033], [15853, 15891], [40004, 40044], [29210, 29236],
      [13411, 13425], [33641, 33678], [40844, 40844], [43488, 43534], [31180, 31183], [17442, 17446], [42305, 42352],
      [23278, 23285], [12760, 12783], [44387, 44404], [30027, 30041], [17803, 17815], [23867, 23876], [21889, 21893],
      [38595, 38629], [41260, 41295], [36284, 36303], [31786, 31826], [19897, 19913], [35108, 35123], [29332, 29370],
      [15339, 15353], [29932, 29982], [25268, 25287], [26442, 26479], [28704, 28741], [32078, 32123], [37885, 37900],
      [39342, 39388], [40335, 40357], [38328, 38366], [18691, 18732], [19704, 19743], [21961, 22009], [26267, 26275],
      [43696, 43708], [12662, 12671], [36980, 37021], [11915, 11947], [23635, 23672], [11552, 11567], [17742, 17792],
      [27524, 27565], [29701, 29732], [12463, 12465], [16237, 16261], [31721, 31735], [30256, 30277], [49587, 49613],
      [14866, 14871], [47214, 47220], [27655, 27702], [49251, 49290], [42603, 42637], [44134, 44175], [12822, 12858],
      [11476, 11524], [12617, 12652], [35012, 35049], [15258, 15301], [27046, 27073], [27402, 27422], [49685, 49709],
      [15176, 15207], [19634, 19671], [34133, 34155], [47128, 47169], [40466, 40466], [21585, 21620], [44220, 44220],
      [14211, 14246], [22976, 23024], [36712, 36737], [45654, 45676], [22909, 22935], [11759, 11771], [49621, 49670],
      [32943, 32978], [22749, 22749], [31758, 31769], [36408, 36450], [13809, 13844], [44752, 44782], [13142, 13173],
      [15987, 15987], [25827, 25828], [27262, 27294], [15567, 15588], [42821, 42862], [21366, 21386], [47041, 47042],
      [38843, 38853], [22461, 22467], [39961, 39966], [38900, 38941], [21658, 21708], [21494, 21496], [44346, 44372],
      [13635, 13651], [41840, 41850], [37051, 37079], [14519, 14552], [15667, 15705], [30048, 30049], [24789, 24824],
      [48541, 48566], [47890, 47929], [44045, 44048], [46689, 46714], [28627, 28658], [15800, 15837], [46261, 46282],
      [46510, 46536], [33442, 33468], [36802, 36816], [26903, 26935], [40371, 40378], [17176, 17219], [30084, 30096],
      [39034, 39056], [46959, 46989], [36126, 36172], [13326, 13360], [26069, 26085], [48194, 48225], [37669, 37697],
      [34529, 34572], [14112, 14122], [43769, 43796], [27305, 27336], [25026, 25070], [15731, 15770], [30810, 30820],
      [33128, 33157], [40597, 40627], [47014, 47015], [13276, 13290], [40573, 40578], [45374, 45416], [34347, 34388],
      [24075, 24079], [47851, 47862], [27868, 27889], [17483, 17516], [14650, 14674], [33184, 33191], [26112, 26143],
      [36850, 36870], [33276, 33324], [17949, 17971], [32522, 32535], [28891, 28908], [15618, 15623], [19096, 19116],
      [35517, 35558], [40868, 40915], [30413, 30440], [19028, 19028], [11873, 11901], [30127, 30136], [19438, 19448],
      [29496, 29510], [27432, 27442], [25836, 25861], [30177, 30224], [27378, 27386], [45190, 45237], [24842, 24887],
      [16179, 16188], [18910, 18954], [39720, 39731], [19587, 19587], [21017, 21020], [15396, 15425], [17597, 17599],
      [28584, 28610], [32711, 32727], [14825, 14826], [15446, 15466], [34312, 34317], [29398, 29402], [42193, 42238],
      [16338, 16384], [35885, 35885], [20784, 20825], [48092, 48098], [21904, 21954], [19777, 19802], [34753, 34767],
      [49426, 49473], [33224, 33244], [13216, 13226], [47337, 47358], [45913, 45939], [24989, 24993], [33956, 34000],
      [29278, 29284], [36077, 36077], [23703, 23709], [14832, 14851], [43391, 43423], [33600, 33619], [39772, 39797],
      [28764, 28782], [23230, 23233], [38264, 38298], [31988, 32033], [13887, 13927], [46805, 46845], [40118, 40147],
      [18329, 18365], [22538, 22542], [25118, 25137], [25943, 25977], [41701, 41705], [39193, 39238], [46908, 46951],
      [22380, 22420], [41537, 41587], [30381, 30400], [42898, 42941], [47960, 48000], [16491, 16539], [12483, 12483],
      [13658, 13706], [18267, 18283], [14249, 14250], [12095, 12098], [39459, 39466], [36330, 36361], [12402, 12451],
      [18807, 18817], [34436, 34452], [49119, 49155], [44913, 44961], [47366, 47379], [16617, 16663], [20983, 21010],
      [46098, 46139], [15596, 15607], [20722, 20745], [16734, 16741], [45755, 45778], [38169, 38217], [25321, 25338],
      [33881, 33912], [20174, 20206], [39562, 39603], [31677, 31702], [28863, 28885], [40225, 40234], [20281, 20302],
      [34619, 34669], [14444, 14492], [24565, 24581], [48143, 48162], [21799, 21836], [41754, 41758], [40091, 40117],
      [17607, 17631], [46310, 46314], [26317, 26326], [18226, 18255], [25899, 25919], [25366, 25411], [11291, 11332],
      [44521, 44554], [44244, 44265], [34911, 34935], [33544, 33568], [25551, 25568], [30955, 30966], [45069, 45093],
      [19945, 19964], [26863, 26866], [36492, 36501], [13093, 13119], [17112, 17136], [35062, 35076], [37572, 37617],
      [38772, 38800], [47612, 47638], [46881, 46886], [37383, 37426], [20327, 20368], [38666, 38668], [34492, 34518],
      [33811, 33842], [17268, 17305], [17869, 17869], [32998, 33000], [15901, 15922], [44054, 44084], [49729, 49741],
      [23313, 23356], [36902, 36933], [36636, 36669], [24745, 24766], [48308, 48309], [28091, 28101], [45432, 45477],
      [27459, 27478], [18066, 18111], [48632, 48637], [15951, 15978], [34786, 34796], [48857, 48905], [34890, 34899],
      [27796, 27818], [42066, 42098]],
     34693, 17465),
    ([[80580, 80593], [69663, 69666], [78718, 78731], [73694, 73694], [51903, 51932], [80075, 80086], [60051, 60072],
      [52798, 52807], [70917, 70924], [75867, 75877], [60831, 60862], [76369, 76411], [52150, 52150], [65898, 65906],
      [69598, 69647], [76248, 76282], [64255, 64299], [70136, 70153], [58156, 58187], [78152, 78169], [83458, 83491],
      [81354, 81380], [56475, 56501], [66317, 66355], [57875, 57905], [82895, 82909], [84104, 84148], [77268, 77276],
      [61180, 61230], [55500, 55539], [53620, 53659], [56005, 56050], [59613, 59625], [60625, 60654], [70940, 70961],
      [61376, 61402], [60115, 60123], [71563, 71608], [59932, 59949], [64079, 64084], [74328, 74334], [64372, 64388],
      [71717, 71730], [60312, 60360], [59086, 59124], [76943, 76966], [84761, 84804], [83752, 83798], [74935, 74937],
      [58508, 58554], [60446, 60471], [68048, 68053], [80868, 80873], [58297, 58301], [84847, 84886], [55174, 55179],
      [76289, 76324], [82193, 82241], [83872, 83911], [62164, 62188], [85371, 85413], [78330, 78338], [84011, 84052],
      [62642, 62649], [56579, 56627], [69016, 69051], [52845, 52894], [74715, 74715], [77407, 77410], [64128, 64158],
      [67690, 67726], [66152, 66189], [62255, 62277], [79538, 79573], [83297, 83346], [59550, 59579], [57238, 57242],
      [60570, 60574], [54547, 54583], [62078, 62122], [66574, 66615], [79392, 79440], [63999, 64045], [69242, 69248],
      [72503, 72542], [69673, 69713], [72865, 72908], [67503, 67534], [77939, 77970], [78536, 78577], [56067, 56093],
      [76753, 76770], [69801, 69844], [59196, 59235], [56319, 56326], [67316, 67362], [70070, 70110], [56263, 56286],
      [56896, 56933], [74887, 74908], [75553, 75574], [73266, 73315], [81292, 81292], [67643, 67643], [52433, 52459],
      [82772, 82808], [69746, 69779], [51419, 51437], [75485, 75497], [70178, 70222], [84985, 84992], [63422, 63452],
      [83802, 83845], [75701, 75748], [69070, 69099], [60726, 60728], [74854, 74863], [52275, 52322], [62313, 62314],
      [51774, 51797], [61846, 61878], [71865, 71903], [72021, 72042], [53486, 53490], [59501, 59510], [71250, 71284],
      [81152, 81184], [73399, 73413], [72815, 72819], [79642, 79685], [52024, 52045], [70806, 70839], [82554, 82593],
      [75050, 75050], [51675, 51679], [79819, 79853], [64759, 64778], [79245, 79294], [73558, 73561], [52747, 52776],
      [64177, 64214], [85101, 85112], [54113, 54124], [66391, 66401], [80517, 80538], [55139, 55159], [79732, 79749],
      [69253, 69271], [56515, 56531], [71925, 71939], [80877, 80921], [70747, 70764], [62744, 62765], [80434, 80450],
      [62508, 62534], [61914, 61926], [72577, 72609], [64508, 64516], [82100, 82102], [84679, 84720], [83963, 84009],
      [75515, 75532], [73948, 73992], [67995, 68005], [51407, 51410], [70229, 70233], [62885, 62907], [75433, 75462],
      [68184, 68193], [80026, 80055], [81935, 81952], [82414, 82459], [51687, 51723], [71526, 71560], [55323, 55372],
      [77367, 77378], [82133, 82164], [82665, 82689], [56975, 56980], [55644, 55686], [62810, 62859], [73903, 73918],
      [66529, 66542], [54368, 54394], [56246, 56254], [67131, 67180], [61688, 61737], [73879, 73896], [72970, 73018],
      [66436, 66458], [73187, 73192], [67584, 67620], [63776, 63822], [55905, 55955], [63525, 63574], [83271, 83273],
      [83712, 83716], [69386, 69411], [52497, 52525], [53110, 53131], [55583, 55607], [80182, 80195], [63164, 63197],
      [71053, 71067], [61100, 61137], [74648, 74698], [54399, 54445], [54827, 54855], [57951, 57958], [56180, 56226],
      [80933, 80954], [59310, 59332], [70457, 70494], [55700, 55726], [53787, 53824], [84485, 84486], [75612, 75625],
      [81602, 81629], [68741, 68759], [72770, 72790], [70039, 70045], [58731, 58773], [66246, 66266], [63022, 63038],
      [83609, 83610], [84438, 84452], [72837, 72855], [81654, 81678], [65933, 65967], [75099, 75118], [70003, 70018],
      [75799, 75826], [78958, 79000], [63338, 63369], [68086, 68091], [63455, 63485], [74468, 74518], [61312, 61350],
      [71019, 71043], [78919, 78919], [80610, 80630], [58037, 58054], [52895, 52936], [76122, 76125], [84055, 84095],
      [63872, 63909], [71402, 71450], [77599, 77638], [69560, 69564], [61641, 61687], [76498, 76534], [74569, 74599],
      [68477, 68507], [57418, 57463], [84229, 84259], [81757, 81782], [59758, 59793], [58910, 58934], [78604, 78636],
      [78215, 78218], [59065, 59072], [75878, 75927], [74162, 74190], [60011, 60031], [68433, 68468], [83077, 83099],
      [59840, 59863], [61968, 61993], [73794, 73843], [68232, 68278], [57644, 57666], [66977, 66997], [84302, 84304],
      [71103, 71153], [80995, 81030], [81813, 81828], [60299, 60311], [69891, 69914], [51548, 51568], [66487, 66511],
      [83575, 83607], [63648, 63683], [76068, 76082], [77529, 77540], [75377, 75386], [77111, 77140], [72699, 72748],
      [82741, 82764], [71799, 71821], [54675, 54719], [64915, 64939], [59630, 59635], [56364, 56372], [66204, 66245],
      [77731, 77775], [64977, 65019], [79345, 79346], [59334, 59340], [79895, 79940], [51478, 51523], [72934, 72958],
      [74754, 74754], [52384, 52390], [65446, 65468], [68612, 68623], [59238, 59278], [81865, 81902], [59961, 60002],
      [56545, 56565], [74257, 74306], [68945, 68975], [52376, 52376], [72450, 72481], [85153, 85194], [84930, 84955],
      [58095, 58117], [59377, 59379], [65527, 65568], [62015, 62036], [53264, 53289], [65049, 65090], [82035, 82059],
      [68704, 68723], [57927, 57934], [80251, 80291], [69507, 69537], [57179, 57203], [72639, 72670], [69454, 69471],
      [73483, 73523], [51829, 51862], [52553, 52570], [83632, 83653], [53947, 53955], [61004, 61033], [57686, 57709],
      [58234, 58253], [74078, 74103], [55028, 55044], [61058, 61086], [53339, 53372], [82247, 82295], [82371, 82391],
      [82487, 82495], [53710, 53742], [85324, 85328], [53523, 53547], [69358, 69381], [58454, 58501], [79183, 79217],
      [59386, 59399], [83369, 83379], [79047, 79048], [68129, 68159], [64350, 64350], [52107, 52107], [67936, 67982],
      [56813, 56814], [80729, 80773], [53086, 53095], [55777, 55806], [74113, 74153], [82692, 82728], [77315, 77319],
      [51875, 51878], [66886, 66934], [81516, 81565], [64799, 64815], [58370, 58392], [80679, 80704], [83424, 83443],
      [58355, 58355], [71633, 71673], [73120, 73137], [65323, 65348], [57347, 57380], [54871, 54888], [57115, 57159],
      [66267, 66313], [74354, 74381], [76168, 76190], [62908, 62931], [85021, 85052], [84190, 84204], [84614, 84641],
      [73241, 73251], [64958, 64958], [64858, 64871], [57909, 57916], [76861, 76873], [70377, 70419], [76819, 76856],
      [59641, 59682], [77673, 77712], [80306, 80343], [79316, 79319], [64467, 64493], [65141, 65188], [85434, 85463],
      [74984, 74998], [83665, 83683], [80297, 80298], [77051, 77080], [79582, 79602], [82506, 82514], [81315, 81315],
      [80131, 80167], [64949, 64956], [83022, 83049], [59721, 59747], [83131, 83141], [75159, 75167], [66521, 66521],
      [51598, 51630], [53889, 53936], [69941, 69955], [77159, 77170], [65917, 65925], [56113, 56151], [65490, 65525],
      [53561, 53571], [76537, 76558], [77435, 77450], [73065, 73106], [70601, 70649], [82923, 82932], [53133, 53173],
      [81109, 81137], [57961, 58003], [75772, 75772], [78117, 78120], [56728, 56734], [52395, 52432], [63045, 63070],
      [76892, 76921], [68780, 68827], [78032, 78067], [74703, 74708], [63690, 63737], [75052, 75093], [54985, 55027],
      [54453, 54497], [57793, 57840], [68374, 68398], [67464, 67498], [65191, 65216], [73650, 73655], [66785, 66791],
      [83510, 83541], [55420, 55468], [58852, 58895], [66796, 66839], [68286, 68286], [68656, 68669], [52653, 52694],
      [54900, 54904], [53213, 53217], [56678, 56719], [75291, 75311], [64642, 64691], [69217, 69228], [73525, 73532],
      [70699, 70737], [79761, 79798], [62345, 62387], [52252, 52269], [58673, 58684], [72144, 72166], [68877, 68910],
      [54188, 54227], [63245, 63271], [75982, 75992], [71004, 71017], [54257, 54274], [66055, 66097], [80350, 80350],
      [61501, 61543], [60776, 60787], [66708, 66739], [82967, 83005], [58604, 58645], [54141, 54141], [58305, 58321],
      [74614, 74620], [85241, 85282], [83234, 83234], [70678, 70683], [61609, 61634], [61441, 61474], [79061, 79105],
      [58787, 58825], [65268, 65276], [68549, 68553], [52578, 52605], [53076, 53081], [78650, 78661], [54728, 54744],
      [52986, 53029], [62973, 62983], [78441, 78480], [53593, 53594], [72396, 72409], [65582, 65609], [62695, 62734],
      [78252, 78289], [65365, 65402], [76217, 76236], [53461, 53474], [75212, 75256], [64413, 64462], [65981, 66030],
      [55849, 55865], [82809, 82831], [71745, 71760], [57626, 57642], [60679, 60680], [78083, 78094], [63750, 63773],
      [62469, 62494], [75044, 75048], [63285, 63319], [74005, 74051], [72350, 72375], [72084, 72105], [52176, 52215],
      [59446, 59491], [52014, 52016], [52708, 52741], [55276, 55289], [64562, 64601], [60225, 60259], [79958, 79975],
      [70262, 70304], [71324, 71334], [55070, 55113], [67287, 67313], [54617, 54637], [77206, 77251], [60940, 60987],
      [58701, 58702], [78852, 78888], [82300, 82339], [73422, 73441], [74803, 74826], [53424, 53437], [65768, 65800],
      [56413, 56452], [78375, 78404], [59886, 59905], [54301, 54340], [78753, 78769], [77000, 77002], [77884, 77911],
      [71379, 71381], [59022, 59036], [54032, 54078], [75334, 75352], [70322, 70347], [76436, 76458], [62558, 62597],
      [62405, 62428], [79122, 79142], [71463, 71488], [61260, 61279], [56857, 56873], [73346, 73349], [71179, 71214],
      [78492, 78523], [74431, 74434], [80465, 80474], [63129, 63136], [60509, 60525], [65839, 65887], [67861, 67908],
      [77813, 77861], [78663, 78697], [77560, 77563], [67077, 67090], [65618, 65659], [76030, 76063], [64712, 64730],
      [81430, 81476], [80793, 80830], [66118, 66122], [63598, 63613], [60382, 60404], [55210, 55251], [57007, 57030],
      [76595, 76644], [57573, 57619], [77477, 77481], [57731, 57763], [74393, 74428], [53838, 53880], [67823, 67824],
      [53967, 53995], [77870, 77871], [72269, 72299], [75963, 75973], [83278, 83279], [75643, 75675], [69114, 69133],
      [53394, 53421], [81072, 81103], [81999, 82007], [67220, 67258], [58294, 58296], [83936, 83961], [54754, 54784],
      [66964, 66970], [60890, 60910], [60160, 60188], [67756, 67786], [68327, 68328], [57508, 57535], [58403, 58408],
      [72212, 72261], [81223, 81256], [59129, 59150], [80196, 80228], [73590, 73600], [57045, 57088], [73023, 73058],
      [52354, 52372], [84348, 84392], [70511, 70540], [81387, 81405], [69293, 69321], [83187, 83223], [66635, 66677],
      [63924, 63960], [78796, 78803], [74209, 74220], [58961, 58981], [81728, 81730], [82838, 82852], [73738, 73779],
      [57293, 57328], [77994, 78031], [70587, 70591], [67402, 67428], [54935, 54976], [67039, 67071], [71943, 71991],
      [52078, 52086], [69152, 69195], [80383, 80408], [68604, 68610], [76681, 76715], [80841, 80849], [78312, 78325],
      [56776, 56797], [63377, 63409], [77787, 77791], [55736, 55743], [70980, 70988], [61779, 61827], [62234, 62250],
      [84529, 84579], [84311, 84344], [79487, 79506], [70859, 70894], [58324, 58343], [82631, 82649], [61588, 61607],
      [63109, 63111], [65704, 65732], [65228, 65267], [51938, 51982]],
     20529, 10709)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumWhiteTiles, cases)

if __name__ == '__main__':
    pass