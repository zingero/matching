import timeit


x = [999, 999, 999]


def foo():
	match x:
		case [0, 0, 0]:
			pass
		case [1, 1, 1]:
			pass
		case [2, 2, 2]:
			pass
		case [3, 3, 3]:
			pass
		case [4, 4, 4]:
			pass
		case [5, 5, 5]:
			pass
		case [6, 6, 6]:
			pass
		case [7, 7, 7]:
			pass
		case [8, 8, 8]:
			pass
		case [9, 9, 9]:
			pass
		case [10, 10, 10]:
			pass
		case [11, 11, 11]:
			pass
		case [12, 12, 12]:
			pass
		case [13, 13, 13]:
			pass
		case [14, 14, 14]:
			pass
		case [15, 15, 15]:
			pass
		case [16, 16, 16]:
			pass
		case [17, 17, 17]:
			pass
		case [18, 18, 18]:
			pass
		case [19, 19, 19]:
			pass
		case [20, 20, 20]:
			pass
		case [21, 21, 21]:
			pass
		case [22, 22, 22]:
			pass
		case [23, 23, 23]:
			pass
		case [24, 24, 24]:
			pass
		case [25, 25, 25]:
			pass
		case [26, 26, 26]:
			pass
		case [27, 27, 27]:
			pass
		case [28, 28, 28]:
			pass
		case [29, 29, 29]:
			pass
		case [30, 30, 30]:
			pass
		case [31, 31, 31]:
			pass
		case [32, 32, 32]:
			pass
		case [33, 33, 33]:
			pass
		case [34, 34, 34]:
			pass
		case [35, 35, 35]:
			pass
		case [36, 36, 36]:
			pass
		case [37, 37, 37]:
			pass
		case [38, 38, 38]:
			pass
		case [39, 39, 39]:
			pass
		case [40, 40, 40]:
			pass
		case [41, 41, 41]:
			pass
		case [42, 42, 42]:
			pass
		case [43, 43, 43]:
			pass
		case [44, 44, 44]:
			pass
		case [45, 45, 45]:
			pass
		case [46, 46, 46]:
			pass
		case [47, 47, 47]:
			pass
		case [48, 48, 48]:
			pass
		case [49, 49, 49]:
			pass
		case [50, 50, 50]:
			pass
		case [51, 51, 51]:
			pass
		case [52, 52, 52]:
			pass
		case [53, 53, 53]:
			pass
		case [54, 54, 54]:
			pass
		case [55, 55, 55]:
			pass
		case [56, 56, 56]:
			pass
		case [57, 57, 57]:
			pass
		case [58, 58, 58]:
			pass
		case [59, 59, 59]:
			pass
		case [60, 60, 60]:
			pass
		case [61, 61, 61]:
			pass
		case [62, 62, 62]:
			pass
		case [63, 63, 63]:
			pass
		case [64, 64, 64]:
			pass
		case [65, 65, 65]:
			pass
		case [66, 66, 66]:
			pass
		case [67, 67, 67]:
			pass
		case [68, 68, 68]:
			pass
		case [69, 69, 69]:
			pass
		case [70, 70, 70]:
			pass
		case [71, 71, 71]:
			pass
		case [72, 72, 72]:
			pass
		case [73, 73, 73]:
			pass
		case [74, 74, 74]:
			pass
		case [75, 75, 75]:
			pass
		case [76, 76, 76]:
			pass
		case [77, 77, 77]:
			pass
		case [78, 78, 78]:
			pass
		case [79, 79, 79]:
			pass
		case [80, 80, 80]:
			pass
		case [81, 81, 81]:
			pass
		case [82, 82, 82]:
			pass
		case [83, 83, 83]:
			pass
		case [84, 84, 84]:
			pass
		case [85, 85, 85]:
			pass
		case [86, 86, 86]:
			pass
		case [87, 87, 87]:
			pass
		case [88, 88, 88]:
			pass
		case [89, 89, 89]:
			pass
		case [90, 90, 90]:
			pass
		case [91, 91, 91]:
			pass
		case [92, 92, 92]:
			pass
		case [93, 93, 93]:
			pass
		case [94, 94, 94]:
			pass
		case [95, 95, 95]:
			pass
		case [96, 96, 96]:
			pass
		case [97, 97, 97]:
			pass
		case [98, 98, 98]:
			pass
		case [99, 99, 99]:
			pass
		case [100, 100, 100]:
			pass
		case [101, 101, 101]:
			pass
		case [102, 102, 102]:
			pass
		case [103, 103, 103]:
			pass
		case [104, 104, 104]:
			pass
		case [105, 105, 105]:
			pass
		case [106, 106, 106]:
			pass
		case [107, 107, 107]:
			pass
		case [108, 108, 108]:
			pass
		case [109, 109, 109]:
			pass
		case [110, 110, 110]:
			pass
		case [111, 111, 111]:
			pass
		case [112, 112, 112]:
			pass
		case [113, 113, 113]:
			pass
		case [114, 114, 114]:
			pass
		case [115, 115, 115]:
			pass
		case [116, 116, 116]:
			pass
		case [117, 117, 117]:
			pass
		case [118, 118, 118]:
			pass
		case [119, 119, 119]:
			pass
		case [120, 120, 120]:
			pass
		case [121, 121, 121]:
			pass
		case [122, 122, 122]:
			pass
		case [123, 123, 123]:
			pass
		case [124, 124, 124]:
			pass
		case [125, 125, 125]:
			pass
		case [126, 126, 126]:
			pass
		case [127, 127, 127]:
			pass
		case [128, 128, 128]:
			pass
		case [129, 129, 129]:
			pass
		case [130, 130, 130]:
			pass
		case [131, 131, 131]:
			pass
		case [132, 132, 132]:
			pass
		case [133, 133, 133]:
			pass
		case [134, 134, 134]:
			pass
		case [135, 135, 135]:
			pass
		case [136, 136, 136]:
			pass
		case [137, 137, 137]:
			pass
		case [138, 138, 138]:
			pass
		case [139, 139, 139]:
			pass
		case [140, 140, 140]:
			pass
		case [141, 141, 141]:
			pass
		case [142, 142, 142]:
			pass
		case [143, 143, 143]:
			pass
		case [144, 144, 144]:
			pass
		case [145, 145, 145]:
			pass
		case [146, 146, 146]:
			pass
		case [147, 147, 147]:
			pass
		case [148, 148, 148]:
			pass
		case [149, 149, 149]:
			pass
		case [150, 150, 150]:
			pass
		case [151, 151, 151]:
			pass
		case [152, 152, 152]:
			pass
		case [153, 153, 153]:
			pass
		case [154, 154, 154]:
			pass
		case [155, 155, 155]:
			pass
		case [156, 156, 156]:
			pass
		case [157, 157, 157]:
			pass
		case [158, 158, 158]:
			pass
		case [159, 159, 159]:
			pass
		case [160, 160, 160]:
			pass
		case [161, 161, 161]:
			pass
		case [162, 162, 162]:
			pass
		case [163, 163, 163]:
			pass
		case [164, 164, 164]:
			pass
		case [165, 165, 165]:
			pass
		case [166, 166, 166]:
			pass
		case [167, 167, 167]:
			pass
		case [168, 168, 168]:
			pass
		case [169, 169, 169]:
			pass
		case [170, 170, 170]:
			pass
		case [171, 171, 171]:
			pass
		case [172, 172, 172]:
			pass
		case [173, 173, 173]:
			pass
		case [174, 174, 174]:
			pass
		case [175, 175, 175]:
			pass
		case [176, 176, 176]:
			pass
		case [177, 177, 177]:
			pass
		case [178, 178, 178]:
			pass
		case [179, 179, 179]:
			pass
		case [180, 180, 180]:
			pass
		case [181, 181, 181]:
			pass
		case [182, 182, 182]:
			pass
		case [183, 183, 183]:
			pass
		case [184, 184, 184]:
			pass
		case [185, 185, 185]:
			pass
		case [186, 186, 186]:
			pass
		case [187, 187, 187]:
			pass
		case [188, 188, 188]:
			pass
		case [189, 189, 189]:
			pass
		case [190, 190, 190]:
			pass
		case [191, 191, 191]:
			pass
		case [192, 192, 192]:
			pass
		case [193, 193, 193]:
			pass
		case [194, 194, 194]:
			pass
		case [195, 195, 195]:
			pass
		case [196, 196, 196]:
			pass
		case [197, 197, 197]:
			pass
		case [198, 198, 198]:
			pass
		case [199, 199, 199]:
			pass
		case [200, 200, 200]:
			pass
		case [201, 201, 201]:
			pass
		case [202, 202, 202]:
			pass
		case [203, 203, 203]:
			pass
		case [204, 204, 204]:
			pass
		case [205, 205, 205]:
			pass
		case [206, 206, 206]:
			pass
		case [207, 207, 207]:
			pass
		case [208, 208, 208]:
			pass
		case [209, 209, 209]:
			pass
		case [210, 210, 210]:
			pass
		case [211, 211, 211]:
			pass
		case [212, 212, 212]:
			pass
		case [213, 213, 213]:
			pass
		case [214, 214, 214]:
			pass
		case [215, 215, 215]:
			pass
		case [216, 216, 216]:
			pass
		case [217, 217, 217]:
			pass
		case [218, 218, 218]:
			pass
		case [219, 219, 219]:
			pass
		case [220, 220, 220]:
			pass
		case [221, 221, 221]:
			pass
		case [222, 222, 222]:
			pass
		case [223, 223, 223]:
			pass
		case [224, 224, 224]:
			pass
		case [225, 225, 225]:
			pass
		case [226, 226, 226]:
			pass
		case [227, 227, 227]:
			pass
		case [228, 228, 228]:
			pass
		case [229, 229, 229]:
			pass
		case [230, 230, 230]:
			pass
		case [231, 231, 231]:
			pass
		case [232, 232, 232]:
			pass
		case [233, 233, 233]:
			pass
		case [234, 234, 234]:
			pass
		case [235, 235, 235]:
			pass
		case [236, 236, 236]:
			pass
		case [237, 237, 237]:
			pass
		case [238, 238, 238]:
			pass
		case [239, 239, 239]:
			pass
		case [240, 240, 240]:
			pass
		case [241, 241, 241]:
			pass
		case [242, 242, 242]:
			pass
		case [243, 243, 243]:
			pass
		case [244, 244, 244]:
			pass
		case [245, 245, 245]:
			pass
		case [246, 246, 246]:
			pass
		case [247, 247, 247]:
			pass
		case [248, 248, 248]:
			pass
		case [249, 249, 249]:
			pass
		case [250, 250, 250]:
			pass
		case [251, 251, 251]:
			pass
		case [252, 252, 252]:
			pass
		case [253, 253, 253]:
			pass
		case [254, 254, 254]:
			pass
		case [255, 255, 255]:
			pass
		case [256, 256, 256]:
			pass
		case [257, 257, 257]:
			pass
		case [258, 258, 258]:
			pass
		case [259, 259, 259]:
			pass
		case [260, 260, 260]:
			pass
		case [261, 261, 261]:
			pass
		case [262, 262, 262]:
			pass
		case [263, 263, 263]:
			pass
		case [264, 264, 264]:
			pass
		case [265, 265, 265]:
			pass
		case [266, 266, 266]:
			pass
		case [267, 267, 267]:
			pass
		case [268, 268, 268]:
			pass
		case [269, 269, 269]:
			pass
		case [270, 270, 270]:
			pass
		case [271, 271, 271]:
			pass
		case [272, 272, 272]:
			pass
		case [273, 273, 273]:
			pass
		case [274, 274, 274]:
			pass
		case [275, 275, 275]:
			pass
		case [276, 276, 276]:
			pass
		case [277, 277, 277]:
			pass
		case [278, 278, 278]:
			pass
		case [279, 279, 279]:
			pass
		case [280, 280, 280]:
			pass
		case [281, 281, 281]:
			pass
		case [282, 282, 282]:
			pass
		case [283, 283, 283]:
			pass
		case [284, 284, 284]:
			pass
		case [285, 285, 285]:
			pass
		case [286, 286, 286]:
			pass
		case [287, 287, 287]:
			pass
		case [288, 288, 288]:
			pass
		case [289, 289, 289]:
			pass
		case [290, 290, 290]:
			pass
		case [291, 291, 291]:
			pass
		case [292, 292, 292]:
			pass
		case [293, 293, 293]:
			pass
		case [294, 294, 294]:
			pass
		case [295, 295, 295]:
			pass
		case [296, 296, 296]:
			pass
		case [297, 297, 297]:
			pass
		case [298, 298, 298]:
			pass
		case [299, 299, 299]:
			pass
		case [300, 300, 300]:
			pass
		case [301, 301, 301]:
			pass
		case [302, 302, 302]:
			pass
		case [303, 303, 303]:
			pass
		case [304, 304, 304]:
			pass
		case [305, 305, 305]:
			pass
		case [306, 306, 306]:
			pass
		case [307, 307, 307]:
			pass
		case [308, 308, 308]:
			pass
		case [309, 309, 309]:
			pass
		case [310, 310, 310]:
			pass
		case [311, 311, 311]:
			pass
		case [312, 312, 312]:
			pass
		case [313, 313, 313]:
			pass
		case [314, 314, 314]:
			pass
		case [315, 315, 315]:
			pass
		case [316, 316, 316]:
			pass
		case [317, 317, 317]:
			pass
		case [318, 318, 318]:
			pass
		case [319, 319, 319]:
			pass
		case [320, 320, 320]:
			pass
		case [321, 321, 321]:
			pass
		case [322, 322, 322]:
			pass
		case [323, 323, 323]:
			pass
		case [324, 324, 324]:
			pass
		case [325, 325, 325]:
			pass
		case [326, 326, 326]:
			pass
		case [327, 327, 327]:
			pass
		case [328, 328, 328]:
			pass
		case [329, 329, 329]:
			pass
		case [330, 330, 330]:
			pass
		case [331, 331, 331]:
			pass
		case [332, 332, 332]:
			pass
		case [333, 333, 333]:
			pass
		case [334, 334, 334]:
			pass
		case [335, 335, 335]:
			pass
		case [336, 336, 336]:
			pass
		case [337, 337, 337]:
			pass
		case [338, 338, 338]:
			pass
		case [339, 339, 339]:
			pass
		case [340, 340, 340]:
			pass
		case [341, 341, 341]:
			pass
		case [342, 342, 342]:
			pass
		case [343, 343, 343]:
			pass
		case [344, 344, 344]:
			pass
		case [345, 345, 345]:
			pass
		case [346, 346, 346]:
			pass
		case [347, 347, 347]:
			pass
		case [348, 348, 348]:
			pass
		case [349, 349, 349]:
			pass
		case [350, 350, 350]:
			pass
		case [351, 351, 351]:
			pass
		case [352, 352, 352]:
			pass
		case [353, 353, 353]:
			pass
		case [354, 354, 354]:
			pass
		case [355, 355, 355]:
			pass
		case [356, 356, 356]:
			pass
		case [357, 357, 357]:
			pass
		case [358, 358, 358]:
			pass
		case [359, 359, 359]:
			pass
		case [360, 360, 360]:
			pass
		case [361, 361, 361]:
			pass
		case [362, 362, 362]:
			pass
		case [363, 363, 363]:
			pass
		case [364, 364, 364]:
			pass
		case [365, 365, 365]:
			pass
		case [366, 366, 366]:
			pass
		case [367, 367, 367]:
			pass
		case [368, 368, 368]:
			pass
		case [369, 369, 369]:
			pass
		case [370, 370, 370]:
			pass
		case [371, 371, 371]:
			pass
		case [372, 372, 372]:
			pass
		case [373, 373, 373]:
			pass
		case [374, 374, 374]:
			pass
		case [375, 375, 375]:
			pass
		case [376, 376, 376]:
			pass
		case [377, 377, 377]:
			pass
		case [378, 378, 378]:
			pass
		case [379, 379, 379]:
			pass
		case [380, 380, 380]:
			pass
		case [381, 381, 381]:
			pass
		case [382, 382, 382]:
			pass
		case [383, 383, 383]:
			pass
		case [384, 384, 384]:
			pass
		case [385, 385, 385]:
			pass
		case [386, 386, 386]:
			pass
		case [387, 387, 387]:
			pass
		case [388, 388, 388]:
			pass
		case [389, 389, 389]:
			pass
		case [390, 390, 390]:
			pass
		case [391, 391, 391]:
			pass
		case [392, 392, 392]:
			pass
		case [393, 393, 393]:
			pass
		case [394, 394, 394]:
			pass
		case [395, 395, 395]:
			pass
		case [396, 396, 396]:
			pass
		case [397, 397, 397]:
			pass
		case [398, 398, 398]:
			pass
		case [399, 399, 399]:
			pass
		case [400, 400, 400]:
			pass
		case [401, 401, 401]:
			pass
		case [402, 402, 402]:
			pass
		case [403, 403, 403]:
			pass
		case [404, 404, 404]:
			pass
		case [405, 405, 405]:
			pass
		case [406, 406, 406]:
			pass
		case [407, 407, 407]:
			pass
		case [408, 408, 408]:
			pass
		case [409, 409, 409]:
			pass
		case [410, 410, 410]:
			pass
		case [411, 411, 411]:
			pass
		case [412, 412, 412]:
			pass
		case [413, 413, 413]:
			pass
		case [414, 414, 414]:
			pass
		case [415, 415, 415]:
			pass
		case [416, 416, 416]:
			pass
		case [417, 417, 417]:
			pass
		case [418, 418, 418]:
			pass
		case [419, 419, 419]:
			pass
		case [420, 420, 420]:
			pass
		case [421, 421, 421]:
			pass
		case [422, 422, 422]:
			pass
		case [423, 423, 423]:
			pass
		case [424, 424, 424]:
			pass
		case [425, 425, 425]:
			pass
		case [426, 426, 426]:
			pass
		case [427, 427, 427]:
			pass
		case [428, 428, 428]:
			pass
		case [429, 429, 429]:
			pass
		case [430, 430, 430]:
			pass
		case [431, 431, 431]:
			pass
		case [432, 432, 432]:
			pass
		case [433, 433, 433]:
			pass
		case [434, 434, 434]:
			pass
		case [435, 435, 435]:
			pass
		case [436, 436, 436]:
			pass
		case [437, 437, 437]:
			pass
		case [438, 438, 438]:
			pass
		case [439, 439, 439]:
			pass
		case [440, 440, 440]:
			pass
		case [441, 441, 441]:
			pass
		case [442, 442, 442]:
			pass
		case [443, 443, 443]:
			pass
		case [444, 444, 444]:
			pass
		case [445, 445, 445]:
			pass
		case [446, 446, 446]:
			pass
		case [447, 447, 447]:
			pass
		case [448, 448, 448]:
			pass
		case [449, 449, 449]:
			pass
		case [450, 450, 450]:
			pass
		case [451, 451, 451]:
			pass
		case [452, 452, 452]:
			pass
		case [453, 453, 453]:
			pass
		case [454, 454, 454]:
			pass
		case [455, 455, 455]:
			pass
		case [456, 456, 456]:
			pass
		case [457, 457, 457]:
			pass
		case [458, 458, 458]:
			pass
		case [459, 459, 459]:
			pass
		case [460, 460, 460]:
			pass
		case [461, 461, 461]:
			pass
		case [462, 462, 462]:
			pass
		case [463, 463, 463]:
			pass
		case [464, 464, 464]:
			pass
		case [465, 465, 465]:
			pass
		case [466, 466, 466]:
			pass
		case [467, 467, 467]:
			pass
		case [468, 468, 468]:
			pass
		case [469, 469, 469]:
			pass
		case [470, 470, 470]:
			pass
		case [471, 471, 471]:
			pass
		case [472, 472, 472]:
			pass
		case [473, 473, 473]:
			pass
		case [474, 474, 474]:
			pass
		case [475, 475, 475]:
			pass
		case [476, 476, 476]:
			pass
		case [477, 477, 477]:
			pass
		case [478, 478, 478]:
			pass
		case [479, 479, 479]:
			pass
		case [480, 480, 480]:
			pass
		case [481, 481, 481]:
			pass
		case [482, 482, 482]:
			pass
		case [483, 483, 483]:
			pass
		case [484, 484, 484]:
			pass
		case [485, 485, 485]:
			pass
		case [486, 486, 486]:
			pass
		case [487, 487, 487]:
			pass
		case [488, 488, 488]:
			pass
		case [489, 489, 489]:
			pass
		case [490, 490, 490]:
			pass
		case [491, 491, 491]:
			pass
		case [492, 492, 492]:
			pass
		case [493, 493, 493]:
			pass
		case [494, 494, 494]:
			pass
		case [495, 495, 495]:
			pass
		case [496, 496, 496]:
			pass
		case [497, 497, 497]:
			pass
		case [498, 498, 498]:
			pass
		case [499, 499, 499]:
			pass
		case [500, 500, 500]:
			pass
		case [501, 501, 501]:
			pass
		case [502, 502, 502]:
			pass
		case [503, 503, 503]:
			pass
		case [504, 504, 504]:
			pass
		case [505, 505, 505]:
			pass
		case [506, 506, 506]:
			pass
		case [507, 507, 507]:
			pass
		case [508, 508, 508]:
			pass
		case [509, 509, 509]:
			pass
		case [510, 510, 510]:
			pass
		case [511, 511, 511]:
			pass
		case [512, 512, 512]:
			pass
		case [513, 513, 513]:
			pass
		case [514, 514, 514]:
			pass
		case [515, 515, 515]:
			pass
		case [516, 516, 516]:
			pass
		case [517, 517, 517]:
			pass
		case [518, 518, 518]:
			pass
		case [519, 519, 519]:
			pass
		case [520, 520, 520]:
			pass
		case [521, 521, 521]:
			pass
		case [522, 522, 522]:
			pass
		case [523, 523, 523]:
			pass
		case [524, 524, 524]:
			pass
		case [525, 525, 525]:
			pass
		case [526, 526, 526]:
			pass
		case [527, 527, 527]:
			pass
		case [528, 528, 528]:
			pass
		case [529, 529, 529]:
			pass
		case [530, 530, 530]:
			pass
		case [531, 531, 531]:
			pass
		case [532, 532, 532]:
			pass
		case [533, 533, 533]:
			pass
		case [534, 534, 534]:
			pass
		case [535, 535, 535]:
			pass
		case [536, 536, 536]:
			pass
		case [537, 537, 537]:
			pass
		case [538, 538, 538]:
			pass
		case [539, 539, 539]:
			pass
		case [540, 540, 540]:
			pass
		case [541, 541, 541]:
			pass
		case [542, 542, 542]:
			pass
		case [543, 543, 543]:
			pass
		case [544, 544, 544]:
			pass
		case [545, 545, 545]:
			pass
		case [546, 546, 546]:
			pass
		case [547, 547, 547]:
			pass
		case [548, 548, 548]:
			pass
		case [549, 549, 549]:
			pass
		case [550, 550, 550]:
			pass
		case [551, 551, 551]:
			pass
		case [552, 552, 552]:
			pass
		case [553, 553, 553]:
			pass
		case [554, 554, 554]:
			pass
		case [555, 555, 555]:
			pass
		case [556, 556, 556]:
			pass
		case [557, 557, 557]:
			pass
		case [558, 558, 558]:
			pass
		case [559, 559, 559]:
			pass
		case [560, 560, 560]:
			pass
		case [561, 561, 561]:
			pass
		case [562, 562, 562]:
			pass
		case [563, 563, 563]:
			pass
		case [564, 564, 564]:
			pass
		case [565, 565, 565]:
			pass
		case [566, 566, 566]:
			pass
		case [567, 567, 567]:
			pass
		case [568, 568, 568]:
			pass
		case [569, 569, 569]:
			pass
		case [570, 570, 570]:
			pass
		case [571, 571, 571]:
			pass
		case [572, 572, 572]:
			pass
		case [573, 573, 573]:
			pass
		case [574, 574, 574]:
			pass
		case [575, 575, 575]:
			pass
		case [576, 576, 576]:
			pass
		case [577, 577, 577]:
			pass
		case [578, 578, 578]:
			pass
		case [579, 579, 579]:
			pass
		case [580, 580, 580]:
			pass
		case [581, 581, 581]:
			pass
		case [582, 582, 582]:
			pass
		case [583, 583, 583]:
			pass
		case [584, 584, 584]:
			pass
		case [585, 585, 585]:
			pass
		case [586, 586, 586]:
			pass
		case [587, 587, 587]:
			pass
		case [588, 588, 588]:
			pass
		case [589, 589, 589]:
			pass
		case [590, 590, 590]:
			pass
		case [591, 591, 591]:
			pass
		case [592, 592, 592]:
			pass
		case [593, 593, 593]:
			pass
		case [594, 594, 594]:
			pass
		case [595, 595, 595]:
			pass
		case [596, 596, 596]:
			pass
		case [597, 597, 597]:
			pass
		case [598, 598, 598]:
			pass
		case [599, 599, 599]:
			pass
		case [600, 600, 600]:
			pass
		case [601, 601, 601]:
			pass
		case [602, 602, 602]:
			pass
		case [603, 603, 603]:
			pass
		case [604, 604, 604]:
			pass
		case [605, 605, 605]:
			pass
		case [606, 606, 606]:
			pass
		case [607, 607, 607]:
			pass
		case [608, 608, 608]:
			pass
		case [609, 609, 609]:
			pass
		case [610, 610, 610]:
			pass
		case [611, 611, 611]:
			pass
		case [612, 612, 612]:
			pass
		case [613, 613, 613]:
			pass
		case [614, 614, 614]:
			pass
		case [615, 615, 615]:
			pass
		case [616, 616, 616]:
			pass
		case [617, 617, 617]:
			pass
		case [618, 618, 618]:
			pass
		case [619, 619, 619]:
			pass
		case [620, 620, 620]:
			pass
		case [621, 621, 621]:
			pass
		case [622, 622, 622]:
			pass
		case [623, 623, 623]:
			pass
		case [624, 624, 624]:
			pass
		case [625, 625, 625]:
			pass
		case [626, 626, 626]:
			pass
		case [627, 627, 627]:
			pass
		case [628, 628, 628]:
			pass
		case [629, 629, 629]:
			pass
		case [630, 630, 630]:
			pass
		case [631, 631, 631]:
			pass
		case [632, 632, 632]:
			pass
		case [633, 633, 633]:
			pass
		case [634, 634, 634]:
			pass
		case [635, 635, 635]:
			pass
		case [636, 636, 636]:
			pass
		case [637, 637, 637]:
			pass
		case [638, 638, 638]:
			pass
		case [639, 639, 639]:
			pass
		case [640, 640, 640]:
			pass
		case [641, 641, 641]:
			pass
		case [642, 642, 642]:
			pass
		case [643, 643, 643]:
			pass
		case [644, 644, 644]:
			pass
		case [645, 645, 645]:
			pass
		case [646, 646, 646]:
			pass
		case [647, 647, 647]:
			pass
		case [648, 648, 648]:
			pass
		case [649, 649, 649]:
			pass
		case [650, 650, 650]:
			pass
		case [651, 651, 651]:
			pass
		case [652, 652, 652]:
			pass
		case [653, 653, 653]:
			pass
		case [654, 654, 654]:
			pass
		case [655, 655, 655]:
			pass
		case [656, 656, 656]:
			pass
		case [657, 657, 657]:
			pass
		case [658, 658, 658]:
			pass
		case [659, 659, 659]:
			pass
		case [660, 660, 660]:
			pass
		case [661, 661, 661]:
			pass
		case [662, 662, 662]:
			pass
		case [663, 663, 663]:
			pass
		case [664, 664, 664]:
			pass
		case [665, 665, 665]:
			pass
		case [666, 666, 666]:
			pass
		case [667, 667, 667]:
			pass
		case [668, 668, 668]:
			pass
		case [669, 669, 669]:
			pass
		case [670, 670, 670]:
			pass
		case [671, 671, 671]:
			pass
		case [672, 672, 672]:
			pass
		case [673, 673, 673]:
			pass
		case [674, 674, 674]:
			pass
		case [675, 675, 675]:
			pass
		case [676, 676, 676]:
			pass
		case [677, 677, 677]:
			pass
		case [678, 678, 678]:
			pass
		case [679, 679, 679]:
			pass
		case [680, 680, 680]:
			pass
		case [681, 681, 681]:
			pass
		case [682, 682, 682]:
			pass
		case [683, 683, 683]:
			pass
		case [684, 684, 684]:
			pass
		case [685, 685, 685]:
			pass
		case [686, 686, 686]:
			pass
		case [687, 687, 687]:
			pass
		case [688, 688, 688]:
			pass
		case [689, 689, 689]:
			pass
		case [690, 690, 690]:
			pass
		case [691, 691, 691]:
			pass
		case [692, 692, 692]:
			pass
		case [693, 693, 693]:
			pass
		case [694, 694, 694]:
			pass
		case [695, 695, 695]:
			pass
		case [696, 696, 696]:
			pass
		case [697, 697, 697]:
			pass
		case [698, 698, 698]:
			pass
		case [699, 699, 699]:
			pass
		case [700, 700, 700]:
			pass
		case [701, 701, 701]:
			pass
		case [702, 702, 702]:
			pass
		case [703, 703, 703]:
			pass
		case [704, 704, 704]:
			pass
		case [705, 705, 705]:
			pass
		case [706, 706, 706]:
			pass
		case [707, 707, 707]:
			pass
		case [708, 708, 708]:
			pass
		case [709, 709, 709]:
			pass
		case [710, 710, 710]:
			pass
		case [711, 711, 711]:
			pass
		case [712, 712, 712]:
			pass
		case [713, 713, 713]:
			pass
		case [714, 714, 714]:
			pass
		case [715, 715, 715]:
			pass
		case [716, 716, 716]:
			pass
		case [717, 717, 717]:
			pass
		case [718, 718, 718]:
			pass
		case [719, 719, 719]:
			pass
		case [720, 720, 720]:
			pass
		case [721, 721, 721]:
			pass
		case [722, 722, 722]:
			pass
		case [723, 723, 723]:
			pass
		case [724, 724, 724]:
			pass
		case [725, 725, 725]:
			pass
		case [726, 726, 726]:
			pass
		case [727, 727, 727]:
			pass
		case [728, 728, 728]:
			pass
		case [729, 729, 729]:
			pass
		case [730, 730, 730]:
			pass
		case [731, 731, 731]:
			pass
		case [732, 732, 732]:
			pass
		case [733, 733, 733]:
			pass
		case [734, 734, 734]:
			pass
		case [735, 735, 735]:
			pass
		case [736, 736, 736]:
			pass
		case [737, 737, 737]:
			pass
		case [738, 738, 738]:
			pass
		case [739, 739, 739]:
			pass
		case [740, 740, 740]:
			pass
		case [741, 741, 741]:
			pass
		case [742, 742, 742]:
			pass
		case [743, 743, 743]:
			pass
		case [744, 744, 744]:
			pass
		case [745, 745, 745]:
			pass
		case [746, 746, 746]:
			pass
		case [747, 747, 747]:
			pass
		case [748, 748, 748]:
			pass
		case [749, 749, 749]:
			pass
		case [750, 750, 750]:
			pass
		case [751, 751, 751]:
			pass
		case [752, 752, 752]:
			pass
		case [753, 753, 753]:
			pass
		case [754, 754, 754]:
			pass
		case [755, 755, 755]:
			pass
		case [756, 756, 756]:
			pass
		case [757, 757, 757]:
			pass
		case [758, 758, 758]:
			pass
		case [759, 759, 759]:
			pass
		case [760, 760, 760]:
			pass
		case [761, 761, 761]:
			pass
		case [762, 762, 762]:
			pass
		case [763, 763, 763]:
			pass
		case [764, 764, 764]:
			pass
		case [765, 765, 765]:
			pass
		case [766, 766, 766]:
			pass
		case [767, 767, 767]:
			pass
		case [768, 768, 768]:
			pass
		case [769, 769, 769]:
			pass
		case [770, 770, 770]:
			pass
		case [771, 771, 771]:
			pass
		case [772, 772, 772]:
			pass
		case [773, 773, 773]:
			pass
		case [774, 774, 774]:
			pass
		case [775, 775, 775]:
			pass
		case [776, 776, 776]:
			pass
		case [777, 777, 777]:
			pass
		case [778, 778, 778]:
			pass
		case [779, 779, 779]:
			pass
		case [780, 780, 780]:
			pass
		case [781, 781, 781]:
			pass
		case [782, 782, 782]:
			pass
		case [783, 783, 783]:
			pass
		case [784, 784, 784]:
			pass
		case [785, 785, 785]:
			pass
		case [786, 786, 786]:
			pass
		case [787, 787, 787]:
			pass
		case [788, 788, 788]:
			pass
		case [789, 789, 789]:
			pass
		case [790, 790, 790]:
			pass
		case [791, 791, 791]:
			pass
		case [792, 792, 792]:
			pass
		case [793, 793, 793]:
			pass
		case [794, 794, 794]:
			pass
		case [795, 795, 795]:
			pass
		case [796, 796, 796]:
			pass
		case [797, 797, 797]:
			pass
		case [798, 798, 798]:
			pass
		case [799, 799, 799]:
			pass
		case [800, 800, 800]:
			pass
		case [801, 801, 801]:
			pass
		case [802, 802, 802]:
			pass
		case [803, 803, 803]:
			pass
		case [804, 804, 804]:
			pass
		case [805, 805, 805]:
			pass
		case [806, 806, 806]:
			pass
		case [807, 807, 807]:
			pass
		case [808, 808, 808]:
			pass
		case [809, 809, 809]:
			pass
		case [810, 810, 810]:
			pass
		case [811, 811, 811]:
			pass
		case [812, 812, 812]:
			pass
		case [813, 813, 813]:
			pass
		case [814, 814, 814]:
			pass
		case [815, 815, 815]:
			pass
		case [816, 816, 816]:
			pass
		case [817, 817, 817]:
			pass
		case [818, 818, 818]:
			pass
		case [819, 819, 819]:
			pass
		case [820, 820, 820]:
			pass
		case [821, 821, 821]:
			pass
		case [822, 822, 822]:
			pass
		case [823, 823, 823]:
			pass
		case [824, 824, 824]:
			pass
		case [825, 825, 825]:
			pass
		case [826, 826, 826]:
			pass
		case [827, 827, 827]:
			pass
		case [828, 828, 828]:
			pass
		case [829, 829, 829]:
			pass
		case [830, 830, 830]:
			pass
		case [831, 831, 831]:
			pass
		case [832, 832, 832]:
			pass
		case [833, 833, 833]:
			pass
		case [834, 834, 834]:
			pass
		case [835, 835, 835]:
			pass
		case [836, 836, 836]:
			pass
		case [837, 837, 837]:
			pass
		case [838, 838, 838]:
			pass
		case [839, 839, 839]:
			pass
		case [840, 840, 840]:
			pass
		case [841, 841, 841]:
			pass
		case [842, 842, 842]:
			pass
		case [843, 843, 843]:
			pass
		case [844, 844, 844]:
			pass
		case [845, 845, 845]:
			pass
		case [846, 846, 846]:
			pass
		case [847, 847, 847]:
			pass
		case [848, 848, 848]:
			pass
		case [849, 849, 849]:
			pass
		case [850, 850, 850]:
			pass
		case [851, 851, 851]:
			pass
		case [852, 852, 852]:
			pass
		case [853, 853, 853]:
			pass
		case [854, 854, 854]:
			pass
		case [855, 855, 855]:
			pass
		case [856, 856, 856]:
			pass
		case [857, 857, 857]:
			pass
		case [858, 858, 858]:
			pass
		case [859, 859, 859]:
			pass
		case [860, 860, 860]:
			pass
		case [861, 861, 861]:
			pass
		case [862, 862, 862]:
			pass
		case [863, 863, 863]:
			pass
		case [864, 864, 864]:
			pass
		case [865, 865, 865]:
			pass
		case [866, 866, 866]:
			pass
		case [867, 867, 867]:
			pass
		case [868, 868, 868]:
			pass
		case [869, 869, 869]:
			pass
		case [870, 870, 870]:
			pass
		case [871, 871, 871]:
			pass
		case [872, 872, 872]:
			pass
		case [873, 873, 873]:
			pass
		case [874, 874, 874]:
			pass
		case [875, 875, 875]:
			pass
		case [876, 876, 876]:
			pass
		case [877, 877, 877]:
			pass
		case [878, 878, 878]:
			pass
		case [879, 879, 879]:
			pass
		case [880, 880, 880]:
			pass
		case [881, 881, 881]:
			pass
		case [882, 882, 882]:
			pass
		case [883, 883, 883]:
			pass
		case [884, 884, 884]:
			pass
		case [885, 885, 885]:
			pass
		case [886, 886, 886]:
			pass
		case [887, 887, 887]:
			pass
		case [888, 888, 888]:
			pass
		case [889, 889, 889]:
			pass
		case [890, 890, 890]:
			pass
		case [891, 891, 891]:
			pass
		case [892, 892, 892]:
			pass
		case [893, 893, 893]:
			pass
		case [894, 894, 894]:
			pass
		case [895, 895, 895]:
			pass
		case [896, 896, 896]:
			pass
		case [897, 897, 897]:
			pass
		case [898, 898, 898]:
			pass
		case [899, 899, 899]:
			pass
		case [900, 900, 900]:
			pass
		case [901, 901, 901]:
			pass
		case [902, 902, 902]:
			pass
		case [903, 903, 903]:
			pass
		case [904, 904, 904]:
			pass
		case [905, 905, 905]:
			pass
		case [906, 906, 906]:
			pass
		case [907, 907, 907]:
			pass
		case [908, 908, 908]:
			pass
		case [909, 909, 909]:
			pass
		case [910, 910, 910]:
			pass
		case [911, 911, 911]:
			pass
		case [912, 912, 912]:
			pass
		case [913, 913, 913]:
			pass
		case [914, 914, 914]:
			pass
		case [915, 915, 915]:
			pass
		case [916, 916, 916]:
			pass
		case [917, 917, 917]:
			pass
		case [918, 918, 918]:
			pass
		case [919, 919, 919]:
			pass
		case [920, 920, 920]:
			pass
		case [921, 921, 921]:
			pass
		case [922, 922, 922]:
			pass
		case [923, 923, 923]:
			pass
		case [924, 924, 924]:
			pass
		case [925, 925, 925]:
			pass
		case [926, 926, 926]:
			pass
		case [927, 927, 927]:
			pass
		case [928, 928, 928]:
			pass
		case [929, 929, 929]:
			pass
		case [930, 930, 930]:
			pass
		case [931, 931, 931]:
			pass
		case [932, 932, 932]:
			pass
		case [933, 933, 933]:
			pass
		case [934, 934, 934]:
			pass
		case [935, 935, 935]:
			pass
		case [936, 936, 936]:
			pass
		case [937, 937, 937]:
			pass
		case [938, 938, 938]:
			pass
		case [939, 939, 939]:
			pass
		case [940, 940, 940]:
			pass
		case [941, 941, 941]:
			pass
		case [942, 942, 942]:
			pass
		case [943, 943, 943]:
			pass
		case [944, 944, 944]:
			pass
		case [945, 945, 945]:
			pass
		case [946, 946, 946]:
			pass
		case [947, 947, 947]:
			pass
		case [948, 948, 948]:
			pass
		case [949, 949, 949]:
			pass
		case [950, 950, 950]:
			pass
		case [951, 951, 951]:
			pass
		case [952, 952, 952]:
			pass
		case [953, 953, 953]:
			pass
		case [954, 954, 954]:
			pass
		case [955, 955, 955]:
			pass
		case [956, 956, 956]:
			pass
		case [957, 957, 957]:
			pass
		case [958, 958, 958]:
			pass
		case [959, 959, 959]:
			pass
		case [960, 960, 960]:
			pass
		case [961, 961, 961]:
			pass
		case [962, 962, 962]:
			pass
		case [963, 963, 963]:
			pass
		case [964, 964, 964]:
			pass
		case [965, 965, 965]:
			pass
		case [966, 966, 966]:
			pass
		case [967, 967, 967]:
			pass
		case [968, 968, 968]:
			pass
		case [969, 969, 969]:
			pass
		case [970, 970, 970]:
			pass
		case [971, 971, 971]:
			pass
		case [972, 972, 972]:
			pass
		case [973, 973, 973]:
			pass
		case [974, 974, 974]:
			pass
		case [975, 975, 975]:
			pass
		case [976, 976, 976]:
			pass
		case [977, 977, 977]:
			pass
		case [978, 978, 978]:
			pass
		case [979, 979, 979]:
			pass
		case [980, 980, 980]:
			pass
		case [981, 981, 981]:
			pass
		case [982, 982, 982]:
			pass
		case [983, 983, 983]:
			pass
		case [984, 984, 984]:
			pass
		case [985, 985, 985]:
			pass
		case [986, 986, 986]:
			pass
		case [987, 987, 987]:
			pass
		case [988, 988, 988]:
			pass
		case [989, 989, 989]:
			pass
		case [990, 990, 990]:
			pass
		case [991, 991, 991]:
			pass
		case [992, 992, 992]:
			pass
		case [993, 993, 993]:
			pass
		case [994, 994, 994]:
			pass
		case [995, 995, 995]:
			pass
		case [996, 996, 996]:
			pass
		case [997, 997, 997]:
			pass
		case [998, 998, 998]:
			pass
		case [999, 999, 999]:
			pass


print(timeit.timeit(foo))  # 62.89494559599552

# for i in range(1000):
# 	print(f"\t\tcase [{i}, {i}, {i}]:\n\t\t\tpass")
