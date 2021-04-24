import timeit
from dataclasses import dataclass


@dataclass()
class A:
	a: int
	b: int

	def __eq__(self, other):
		return self.a == other.a and self.b == other.b


a = A(999, 999)


def foo():
	if a == A(0, 0):
		pass
	elif a == A(1, 1):
		pass
	elif a == A(2, 2):
		pass
	elif a == A(3, 3):
		pass
	elif a == A(4, 4):
		pass
	elif a == A(5, 5):
		pass
	elif a == A(6, 6):
		pass
	elif a == A(7, 7):
		pass
	elif a == A(8, 8):
		pass
	elif a == A(9, 9):
		pass
	elif a == A(10, 10):
		pass
	elif a == A(11, 11):
		pass
	elif a == A(12, 12):
		pass
	elif a == A(13, 13):
		pass
	elif a == A(14, 14):
		pass
	elif a == A(15, 15):
		pass
	elif a == A(16, 16):
		pass
	elif a == A(17, 17):
		pass
	elif a == A(18, 18):
		pass
	elif a == A(19, 19):
		pass
	elif a == A(20, 20):
		pass
	elif a == A(21, 21):
		pass
	elif a == A(22, 22):
		pass
	elif a == A(23, 23):
		pass
	elif a == A(24, 24):
		pass
	elif a == A(25, 25):
		pass
	elif a == A(26, 26):
		pass
	elif a == A(27, 27):
		pass
	elif a == A(28, 28):
		pass
	elif a == A(29, 29):
		pass
	elif a == A(30, 30):
		pass
	elif a == A(31, 31):
		pass
	elif a == A(32, 32):
		pass
	elif a == A(33, 33):
		pass
	elif a == A(34, 34):
		pass
	elif a == A(35, 35):
		pass
	elif a == A(36, 36):
		pass
	elif a == A(37, 37):
		pass
	elif a == A(38, 38):
		pass
	elif a == A(39, 39):
		pass
	elif a == A(40, 40):
		pass
	elif a == A(41, 41):
		pass
	elif a == A(42, 42):
		pass
	elif a == A(43, 43):
		pass
	elif a == A(44, 44):
		pass
	elif a == A(45, 45):
		pass
	elif a == A(46, 46):
		pass
	elif a == A(47, 47):
		pass
	elif a == A(48, 48):
		pass
	elif a == A(49, 49):
		pass
	elif a == A(50, 50):
		pass
	elif a == A(51, 51):
		pass
	elif a == A(52, 52):
		pass
	elif a == A(53, 53):
		pass
	elif a == A(54, 54):
		pass
	elif a == A(55, 55):
		pass
	elif a == A(56, 56):
		pass
	elif a == A(57, 57):
		pass
	elif a == A(58, 58):
		pass
	elif a == A(59, 59):
		pass
	elif a == A(60, 60):
		pass
	elif a == A(61, 61):
		pass
	elif a == A(62, 62):
		pass
	elif a == A(63, 63):
		pass
	elif a == A(64, 64):
		pass
	elif a == A(65, 65):
		pass
	elif a == A(66, 66):
		pass
	elif a == A(67, 67):
		pass
	elif a == A(68, 68):
		pass
	elif a == A(69, 69):
		pass
	elif a == A(70, 70):
		pass
	elif a == A(71, 71):
		pass
	elif a == A(72, 72):
		pass
	elif a == A(73, 73):
		pass
	elif a == A(74, 74):
		pass
	elif a == A(75, 75):
		pass
	elif a == A(76, 76):
		pass
	elif a == A(77, 77):
		pass
	elif a == A(78, 78):
		pass
	elif a == A(79, 79):
		pass
	elif a == A(80, 80):
		pass
	elif a == A(81, 81):
		pass
	elif a == A(82, 82):
		pass
	elif a == A(83, 83):
		pass
	elif a == A(84, 84):
		pass
	elif a == A(85, 85):
		pass
	elif a == A(86, 86):
		pass
	elif a == A(87, 87):
		pass
	elif a == A(88, 88):
		pass
	elif a == A(89, 89):
		pass
	elif a == A(90, 90):
		pass
	elif a == A(91, 91):
		pass
	elif a == A(92, 92):
		pass
	elif a == A(93, 93):
		pass
	elif a == A(94, 94):
		pass
	elif a == A(95, 95):
		pass
	elif a == A(96, 96):
		pass
	elif a == A(97, 97):
		pass
	elif a == A(98, 98):
		pass
	elif a == A(99, 99):
		pass
	elif a == A(100, 100):
		pass
	elif a == A(101, 101):
		pass
	elif a == A(102, 102):
		pass
	elif a == A(103, 103):
		pass
	elif a == A(104, 104):
		pass
	elif a == A(105, 105):
		pass
	elif a == A(106, 106):
		pass
	elif a == A(107, 107):
		pass
	elif a == A(108, 108):
		pass
	elif a == A(109, 109):
		pass
	elif a == A(110, 110):
		pass
	elif a == A(111, 111):
		pass
	elif a == A(112, 112):
		pass
	elif a == A(113, 113):
		pass
	elif a == A(114, 114):
		pass
	elif a == A(115, 115):
		pass
	elif a == A(116, 116):
		pass
	elif a == A(117, 117):
		pass
	elif a == A(118, 118):
		pass
	elif a == A(119, 119):
		pass
	elif a == A(120, 120):
		pass
	elif a == A(121, 121):
		pass
	elif a == A(122, 122):
		pass
	elif a == A(123, 123):
		pass
	elif a == A(124, 124):
		pass
	elif a == A(125, 125):
		pass
	elif a == A(126, 126):
		pass
	elif a == A(127, 127):
		pass
	elif a == A(128, 128):
		pass
	elif a == A(129, 129):
		pass
	elif a == A(130, 130):
		pass
	elif a == A(131, 131):
		pass
	elif a == A(132, 132):
		pass
	elif a == A(133, 133):
		pass
	elif a == A(134, 134):
		pass
	elif a == A(135, 135):
		pass
	elif a == A(136, 136):
		pass
	elif a == A(137, 137):
		pass
	elif a == A(138, 138):
		pass
	elif a == A(139, 139):
		pass
	elif a == A(140, 140):
		pass
	elif a == A(141, 141):
		pass
	elif a == A(142, 142):
		pass
	elif a == A(143, 143):
		pass
	elif a == A(144, 144):
		pass
	elif a == A(145, 145):
		pass
	elif a == A(146, 146):
		pass
	elif a == A(147, 147):
		pass
	elif a == A(148, 148):
		pass
	elif a == A(149, 149):
		pass
	elif a == A(150, 150):
		pass
	elif a == A(151, 151):
		pass
	elif a == A(152, 152):
		pass
	elif a == A(153, 153):
		pass
	elif a == A(154, 154):
		pass
	elif a == A(155, 155):
		pass
	elif a == A(156, 156):
		pass
	elif a == A(157, 157):
		pass
	elif a == A(158, 158):
		pass
	elif a == A(159, 159):
		pass
	elif a == A(160, 160):
		pass
	elif a == A(161, 161):
		pass
	elif a == A(162, 162):
		pass
	elif a == A(163, 163):
		pass
	elif a == A(164, 164):
		pass
	elif a == A(165, 165):
		pass
	elif a == A(166, 166):
		pass
	elif a == A(167, 167):
		pass
	elif a == A(168, 168):
		pass
	elif a == A(169, 169):
		pass
	elif a == A(170, 170):
		pass
	elif a == A(171, 171):
		pass
	elif a == A(172, 172):
		pass
	elif a == A(173, 173):
		pass
	elif a == A(174, 174):
		pass
	elif a == A(175, 175):
		pass
	elif a == A(176, 176):
		pass
	elif a == A(177, 177):
		pass
	elif a == A(178, 178):
		pass
	elif a == A(179, 179):
		pass
	elif a == A(180, 180):
		pass
	elif a == A(181, 181):
		pass
	elif a == A(182, 182):
		pass
	elif a == A(183, 183):
		pass
	elif a == A(184, 184):
		pass
	elif a == A(185, 185):
		pass
	elif a == A(186, 186):
		pass
	elif a == A(187, 187):
		pass
	elif a == A(188, 188):
		pass
	elif a == A(189, 189):
		pass
	elif a == A(190, 190):
		pass
	elif a == A(191, 191):
		pass
	elif a == A(192, 192):
		pass
	elif a == A(193, 193):
		pass
	elif a == A(194, 194):
		pass
	elif a == A(195, 195):
		pass
	elif a == A(196, 196):
		pass
	elif a == A(197, 197):
		pass
	elif a == A(198, 198):
		pass
	elif a == A(199, 199):
		pass
	elif a == A(200, 200):
		pass
	elif a == A(201, 201):
		pass
	elif a == A(202, 202):
		pass
	elif a == A(203, 203):
		pass
	elif a == A(204, 204):
		pass
	elif a == A(205, 205):
		pass
	elif a == A(206, 206):
		pass
	elif a == A(207, 207):
		pass
	elif a == A(208, 208):
		pass
	elif a == A(209, 209):
		pass
	elif a == A(210, 210):
		pass
	elif a == A(211, 211):
		pass
	elif a == A(212, 212):
		pass
	elif a == A(213, 213):
		pass
	elif a == A(214, 214):
		pass
	elif a == A(215, 215):
		pass
	elif a == A(216, 216):
		pass
	elif a == A(217, 217):
		pass
	elif a == A(218, 218):
		pass
	elif a == A(219, 219):
		pass
	elif a == A(220, 220):
		pass
	elif a == A(221, 221):
		pass
	elif a == A(222, 222):
		pass
	elif a == A(223, 223):
		pass
	elif a == A(224, 224):
		pass
	elif a == A(225, 225):
		pass
	elif a == A(226, 226):
		pass
	elif a == A(227, 227):
		pass
	elif a == A(228, 228):
		pass
	elif a == A(229, 229):
		pass
	elif a == A(230, 230):
		pass
	elif a == A(231, 231):
		pass
	elif a == A(232, 232):
		pass
	elif a == A(233, 233):
		pass
	elif a == A(234, 234):
		pass
	elif a == A(235, 235):
		pass
	elif a == A(236, 236):
		pass
	elif a == A(237, 237):
		pass
	elif a == A(238, 238):
		pass
	elif a == A(239, 239):
		pass
	elif a == A(240, 240):
		pass
	elif a == A(241, 241):
		pass
	elif a == A(242, 242):
		pass
	elif a == A(243, 243):
		pass
	elif a == A(244, 244):
		pass
	elif a == A(245, 245):
		pass
	elif a == A(246, 246):
		pass
	elif a == A(247, 247):
		pass
	elif a == A(248, 248):
		pass
	elif a == A(249, 249):
		pass
	elif a == A(250, 250):
		pass
	elif a == A(251, 251):
		pass
	elif a == A(252, 252):
		pass
	elif a == A(253, 253):
		pass
	elif a == A(254, 254):
		pass
	elif a == A(255, 255):
		pass
	elif a == A(256, 256):
		pass
	elif a == A(257, 257):
		pass
	elif a == A(258, 258):
		pass
	elif a == A(259, 259):
		pass
	elif a == A(260, 260):
		pass
	elif a == A(261, 261):
		pass
	elif a == A(262, 262):
		pass
	elif a == A(263, 263):
		pass
	elif a == A(264, 264):
		pass
	elif a == A(265, 265):
		pass
	elif a == A(266, 266):
		pass
	elif a == A(267, 267):
		pass
	elif a == A(268, 268):
		pass
	elif a == A(269, 269):
		pass
	elif a == A(270, 270):
		pass
	elif a == A(271, 271):
		pass
	elif a == A(272, 272):
		pass
	elif a == A(273, 273):
		pass
	elif a == A(274, 274):
		pass
	elif a == A(275, 275):
		pass
	elif a == A(276, 276):
		pass
	elif a == A(277, 277):
		pass
	elif a == A(278, 278):
		pass
	elif a == A(279, 279):
		pass
	elif a == A(280, 280):
		pass
	elif a == A(281, 281):
		pass
	elif a == A(282, 282):
		pass
	elif a == A(283, 283):
		pass
	elif a == A(284, 284):
		pass
	elif a == A(285, 285):
		pass
	elif a == A(286, 286):
		pass
	elif a == A(287, 287):
		pass
	elif a == A(288, 288):
		pass
	elif a == A(289, 289):
		pass
	elif a == A(290, 290):
		pass
	elif a == A(291, 291):
		pass
	elif a == A(292, 292):
		pass
	elif a == A(293, 293):
		pass
	elif a == A(294, 294):
		pass
	elif a == A(295, 295):
		pass
	elif a == A(296, 296):
		pass
	elif a == A(297, 297):
		pass
	elif a == A(298, 298):
		pass
	elif a == A(299, 299):
		pass
	elif a == A(300, 300):
		pass
	elif a == A(301, 301):
		pass
	elif a == A(302, 302):
		pass
	elif a == A(303, 303):
		pass
	elif a == A(304, 304):
		pass
	elif a == A(305, 305):
		pass
	elif a == A(306, 306):
		pass
	elif a == A(307, 307):
		pass
	elif a == A(308, 308):
		pass
	elif a == A(309, 309):
		pass
	elif a == A(310, 310):
		pass
	elif a == A(311, 311):
		pass
	elif a == A(312, 312):
		pass
	elif a == A(313, 313):
		pass
	elif a == A(314, 314):
		pass
	elif a == A(315, 315):
		pass
	elif a == A(316, 316):
		pass
	elif a == A(317, 317):
		pass
	elif a == A(318, 318):
		pass
	elif a == A(319, 319):
		pass
	elif a == A(320, 320):
		pass
	elif a == A(321, 321):
		pass
	elif a == A(322, 322):
		pass
	elif a == A(323, 323):
		pass
	elif a == A(324, 324):
		pass
	elif a == A(325, 325):
		pass
	elif a == A(326, 326):
		pass
	elif a == A(327, 327):
		pass
	elif a == A(328, 328):
		pass
	elif a == A(329, 329):
		pass
	elif a == A(330, 330):
		pass
	elif a == A(331, 331):
		pass
	elif a == A(332, 332):
		pass
	elif a == A(333, 333):
		pass
	elif a == A(334, 334):
		pass
	elif a == A(335, 335):
		pass
	elif a == A(336, 336):
		pass
	elif a == A(337, 337):
		pass
	elif a == A(338, 338):
		pass
	elif a == A(339, 339):
		pass
	elif a == A(340, 340):
		pass
	elif a == A(341, 341):
		pass
	elif a == A(342, 342):
		pass
	elif a == A(343, 343):
		pass
	elif a == A(344, 344):
		pass
	elif a == A(345, 345):
		pass
	elif a == A(346, 346):
		pass
	elif a == A(347, 347):
		pass
	elif a == A(348, 348):
		pass
	elif a == A(349, 349):
		pass
	elif a == A(350, 350):
		pass
	elif a == A(351, 351):
		pass
	elif a == A(352, 352):
		pass
	elif a == A(353, 353):
		pass
	elif a == A(354, 354):
		pass
	elif a == A(355, 355):
		pass
	elif a == A(356, 356):
		pass
	elif a == A(357, 357):
		pass
	elif a == A(358, 358):
		pass
	elif a == A(359, 359):
		pass
	elif a == A(360, 360):
		pass
	elif a == A(361, 361):
		pass
	elif a == A(362, 362):
		pass
	elif a == A(363, 363):
		pass
	elif a == A(364, 364):
		pass
	elif a == A(365, 365):
		pass
	elif a == A(366, 366):
		pass
	elif a == A(367, 367):
		pass
	elif a == A(368, 368):
		pass
	elif a == A(369, 369):
		pass
	elif a == A(370, 370):
		pass
	elif a == A(371, 371):
		pass
	elif a == A(372, 372):
		pass
	elif a == A(373, 373):
		pass
	elif a == A(374, 374):
		pass
	elif a == A(375, 375):
		pass
	elif a == A(376, 376):
		pass
	elif a == A(377, 377):
		pass
	elif a == A(378, 378):
		pass
	elif a == A(379, 379):
		pass
	elif a == A(380, 380):
		pass
	elif a == A(381, 381):
		pass
	elif a == A(382, 382):
		pass
	elif a == A(383, 383):
		pass
	elif a == A(384, 384):
		pass
	elif a == A(385, 385):
		pass
	elif a == A(386, 386):
		pass
	elif a == A(387, 387):
		pass
	elif a == A(388, 388):
		pass
	elif a == A(389, 389):
		pass
	elif a == A(390, 390):
		pass
	elif a == A(391, 391):
		pass
	elif a == A(392, 392):
		pass
	elif a == A(393, 393):
		pass
	elif a == A(394, 394):
		pass
	elif a == A(395, 395):
		pass
	elif a == A(396, 396):
		pass
	elif a == A(397, 397):
		pass
	elif a == A(398, 398):
		pass
	elif a == A(399, 399):
		pass
	elif a == A(400, 400):
		pass
	elif a == A(401, 401):
		pass
	elif a == A(402, 402):
		pass
	elif a == A(403, 403):
		pass
	elif a == A(404, 404):
		pass
	elif a == A(405, 405):
		pass
	elif a == A(406, 406):
		pass
	elif a == A(407, 407):
		pass
	elif a == A(408, 408):
		pass
	elif a == A(409, 409):
		pass
	elif a == A(410, 410):
		pass
	elif a == A(411, 411):
		pass
	elif a == A(412, 412):
		pass
	elif a == A(413, 413):
		pass
	elif a == A(414, 414):
		pass
	elif a == A(415, 415):
		pass
	elif a == A(416, 416):
		pass
	elif a == A(417, 417):
		pass
	elif a == A(418, 418):
		pass
	elif a == A(419, 419):
		pass
	elif a == A(420, 420):
		pass
	elif a == A(421, 421):
		pass
	elif a == A(422, 422):
		pass
	elif a == A(423, 423):
		pass
	elif a == A(424, 424):
		pass
	elif a == A(425, 425):
		pass
	elif a == A(426, 426):
		pass
	elif a == A(427, 427):
		pass
	elif a == A(428, 428):
		pass
	elif a == A(429, 429):
		pass
	elif a == A(430, 430):
		pass
	elif a == A(431, 431):
		pass
	elif a == A(432, 432):
		pass
	elif a == A(433, 433):
		pass
	elif a == A(434, 434):
		pass
	elif a == A(435, 435):
		pass
	elif a == A(436, 436):
		pass
	elif a == A(437, 437):
		pass
	elif a == A(438, 438):
		pass
	elif a == A(439, 439):
		pass
	elif a == A(440, 440):
		pass
	elif a == A(441, 441):
		pass
	elif a == A(442, 442):
		pass
	elif a == A(443, 443):
		pass
	elif a == A(444, 444):
		pass
	elif a == A(445, 445):
		pass
	elif a == A(446, 446):
		pass
	elif a == A(447, 447):
		pass
	elif a == A(448, 448):
		pass
	elif a == A(449, 449):
		pass
	elif a == A(450, 450):
		pass
	elif a == A(451, 451):
		pass
	elif a == A(452, 452):
		pass
	elif a == A(453, 453):
		pass
	elif a == A(454, 454):
		pass
	elif a == A(455, 455):
		pass
	elif a == A(456, 456):
		pass
	elif a == A(457, 457):
		pass
	elif a == A(458, 458):
		pass
	elif a == A(459, 459):
		pass
	elif a == A(460, 460):
		pass
	elif a == A(461, 461):
		pass
	elif a == A(462, 462):
		pass
	elif a == A(463, 463):
		pass
	elif a == A(464, 464):
		pass
	elif a == A(465, 465):
		pass
	elif a == A(466, 466):
		pass
	elif a == A(467, 467):
		pass
	elif a == A(468, 468):
		pass
	elif a == A(469, 469):
		pass
	elif a == A(470, 470):
		pass
	elif a == A(471, 471):
		pass
	elif a == A(472, 472):
		pass
	elif a == A(473, 473):
		pass
	elif a == A(474, 474):
		pass
	elif a == A(475, 475):
		pass
	elif a == A(476, 476):
		pass
	elif a == A(477, 477):
		pass
	elif a == A(478, 478):
		pass
	elif a == A(479, 479):
		pass
	elif a == A(480, 480):
		pass
	elif a == A(481, 481):
		pass
	elif a == A(482, 482):
		pass
	elif a == A(483, 483):
		pass
	elif a == A(484, 484):
		pass
	elif a == A(485, 485):
		pass
	elif a == A(486, 486):
		pass
	elif a == A(487, 487):
		pass
	elif a == A(488, 488):
		pass
	elif a == A(489, 489):
		pass
	elif a == A(490, 490):
		pass
	elif a == A(491, 491):
		pass
	elif a == A(492, 492):
		pass
	elif a == A(493, 493):
		pass
	elif a == A(494, 494):
		pass
	elif a == A(495, 495):
		pass
	elif a == A(496, 496):
		pass
	elif a == A(497, 497):
		pass
	elif a == A(498, 498):
		pass
	elif a == A(499, 499):
		pass
	elif a == A(500, 500):
		pass
	elif a == A(501, 501):
		pass
	elif a == A(502, 502):
		pass
	elif a == A(503, 503):
		pass
	elif a == A(504, 504):
		pass
	elif a == A(505, 505):
		pass
	elif a == A(506, 506):
		pass
	elif a == A(507, 507):
		pass
	elif a == A(508, 508):
		pass
	elif a == A(509, 509):
		pass
	elif a == A(510, 510):
		pass
	elif a == A(511, 511):
		pass
	elif a == A(512, 512):
		pass
	elif a == A(513, 513):
		pass
	elif a == A(514, 514):
		pass
	elif a == A(515, 515):
		pass
	elif a == A(516, 516):
		pass
	elif a == A(517, 517):
		pass
	elif a == A(518, 518):
		pass
	elif a == A(519, 519):
		pass
	elif a == A(520, 520):
		pass
	elif a == A(521, 521):
		pass
	elif a == A(522, 522):
		pass
	elif a == A(523, 523):
		pass
	elif a == A(524, 524):
		pass
	elif a == A(525, 525):
		pass
	elif a == A(526, 526):
		pass
	elif a == A(527, 527):
		pass
	elif a == A(528, 528):
		pass
	elif a == A(529, 529):
		pass
	elif a == A(530, 530):
		pass
	elif a == A(531, 531):
		pass
	elif a == A(532, 532):
		pass
	elif a == A(533, 533):
		pass
	elif a == A(534, 534):
		pass
	elif a == A(535, 535):
		pass
	elif a == A(536, 536):
		pass
	elif a == A(537, 537):
		pass
	elif a == A(538, 538):
		pass
	elif a == A(539, 539):
		pass
	elif a == A(540, 540):
		pass
	elif a == A(541, 541):
		pass
	elif a == A(542, 542):
		pass
	elif a == A(543, 543):
		pass
	elif a == A(544, 544):
		pass
	elif a == A(545, 545):
		pass
	elif a == A(546, 546):
		pass
	elif a == A(547, 547):
		pass
	elif a == A(548, 548):
		pass
	elif a == A(549, 549):
		pass
	elif a == A(550, 550):
		pass
	elif a == A(551, 551):
		pass
	elif a == A(552, 552):
		pass
	elif a == A(553, 553):
		pass
	elif a == A(554, 554):
		pass
	elif a == A(555, 555):
		pass
	elif a == A(556, 556):
		pass
	elif a == A(557, 557):
		pass
	elif a == A(558, 558):
		pass
	elif a == A(559, 559):
		pass
	elif a == A(560, 560):
		pass
	elif a == A(561, 561):
		pass
	elif a == A(562, 562):
		pass
	elif a == A(563, 563):
		pass
	elif a == A(564, 564):
		pass
	elif a == A(565, 565):
		pass
	elif a == A(566, 566):
		pass
	elif a == A(567, 567):
		pass
	elif a == A(568, 568):
		pass
	elif a == A(569, 569):
		pass
	elif a == A(570, 570):
		pass
	elif a == A(571, 571):
		pass
	elif a == A(572, 572):
		pass
	elif a == A(573, 573):
		pass
	elif a == A(574, 574):
		pass
	elif a == A(575, 575):
		pass
	elif a == A(576, 576):
		pass
	elif a == A(577, 577):
		pass
	elif a == A(578, 578):
		pass
	elif a == A(579, 579):
		pass
	elif a == A(580, 580):
		pass
	elif a == A(581, 581):
		pass
	elif a == A(582, 582):
		pass
	elif a == A(583, 583):
		pass
	elif a == A(584, 584):
		pass
	elif a == A(585, 585):
		pass
	elif a == A(586, 586):
		pass
	elif a == A(587, 587):
		pass
	elif a == A(588, 588):
		pass
	elif a == A(589, 589):
		pass
	elif a == A(590, 590):
		pass
	elif a == A(591, 591):
		pass
	elif a == A(592, 592):
		pass
	elif a == A(593, 593):
		pass
	elif a == A(594, 594):
		pass
	elif a == A(595, 595):
		pass
	elif a == A(596, 596):
		pass
	elif a == A(597, 597):
		pass
	elif a == A(598, 598):
		pass
	elif a == A(599, 599):
		pass
	elif a == A(600, 600):
		pass
	elif a == A(601, 601):
		pass
	elif a == A(602, 602):
		pass
	elif a == A(603, 603):
		pass
	elif a == A(604, 604):
		pass
	elif a == A(605, 605):
		pass
	elif a == A(606, 606):
		pass
	elif a == A(607, 607):
		pass
	elif a == A(608, 608):
		pass
	elif a == A(609, 609):
		pass
	elif a == A(610, 610):
		pass
	elif a == A(611, 611):
		pass
	elif a == A(612, 612):
		pass
	elif a == A(613, 613):
		pass
	elif a == A(614, 614):
		pass
	elif a == A(615, 615):
		pass
	elif a == A(616, 616):
		pass
	elif a == A(617, 617):
		pass
	elif a == A(618, 618):
		pass
	elif a == A(619, 619):
		pass
	elif a == A(620, 620):
		pass
	elif a == A(621, 621):
		pass
	elif a == A(622, 622):
		pass
	elif a == A(623, 623):
		pass
	elif a == A(624, 624):
		pass
	elif a == A(625, 625):
		pass
	elif a == A(626, 626):
		pass
	elif a == A(627, 627):
		pass
	elif a == A(628, 628):
		pass
	elif a == A(629, 629):
		pass
	elif a == A(630, 630):
		pass
	elif a == A(631, 631):
		pass
	elif a == A(632, 632):
		pass
	elif a == A(633, 633):
		pass
	elif a == A(634, 634):
		pass
	elif a == A(635, 635):
		pass
	elif a == A(636, 636):
		pass
	elif a == A(637, 637):
		pass
	elif a == A(638, 638):
		pass
	elif a == A(639, 639):
		pass
	elif a == A(640, 640):
		pass
	elif a == A(641, 641):
		pass
	elif a == A(642, 642):
		pass
	elif a == A(643, 643):
		pass
	elif a == A(644, 644):
		pass
	elif a == A(645, 645):
		pass
	elif a == A(646, 646):
		pass
	elif a == A(647, 647):
		pass
	elif a == A(648, 648):
		pass
	elif a == A(649, 649):
		pass
	elif a == A(650, 650):
		pass
	elif a == A(651, 651):
		pass
	elif a == A(652, 652):
		pass
	elif a == A(653, 653):
		pass
	elif a == A(654, 654):
		pass
	elif a == A(655, 655):
		pass
	elif a == A(656, 656):
		pass
	elif a == A(657, 657):
		pass
	elif a == A(658, 658):
		pass
	elif a == A(659, 659):
		pass
	elif a == A(660, 660):
		pass
	elif a == A(661, 661):
		pass
	elif a == A(662, 662):
		pass
	elif a == A(663, 663):
		pass
	elif a == A(664, 664):
		pass
	elif a == A(665, 665):
		pass
	elif a == A(666, 666):
		pass
	elif a == A(667, 667):
		pass
	elif a == A(668, 668):
		pass
	elif a == A(669, 669):
		pass
	elif a == A(670, 670):
		pass
	elif a == A(671, 671):
		pass
	elif a == A(672, 672):
		pass
	elif a == A(673, 673):
		pass
	elif a == A(674, 674):
		pass
	elif a == A(675, 675):
		pass
	elif a == A(676, 676):
		pass
	elif a == A(677, 677):
		pass
	elif a == A(678, 678):
		pass
	elif a == A(679, 679):
		pass
	elif a == A(680, 680):
		pass
	elif a == A(681, 681):
		pass
	elif a == A(682, 682):
		pass
	elif a == A(683, 683):
		pass
	elif a == A(684, 684):
		pass
	elif a == A(685, 685):
		pass
	elif a == A(686, 686):
		pass
	elif a == A(687, 687):
		pass
	elif a == A(688, 688):
		pass
	elif a == A(689, 689):
		pass
	elif a == A(690, 690):
		pass
	elif a == A(691, 691):
		pass
	elif a == A(692, 692):
		pass
	elif a == A(693, 693):
		pass
	elif a == A(694, 694):
		pass
	elif a == A(695, 695):
		pass
	elif a == A(696, 696):
		pass
	elif a == A(697, 697):
		pass
	elif a == A(698, 698):
		pass
	elif a == A(699, 699):
		pass
	elif a == A(700, 700):
		pass
	elif a == A(701, 701):
		pass
	elif a == A(702, 702):
		pass
	elif a == A(703, 703):
		pass
	elif a == A(704, 704):
		pass
	elif a == A(705, 705):
		pass
	elif a == A(706, 706):
		pass
	elif a == A(707, 707):
		pass
	elif a == A(708, 708):
		pass
	elif a == A(709, 709):
		pass
	elif a == A(710, 710):
		pass
	elif a == A(711, 711):
		pass
	elif a == A(712, 712):
		pass
	elif a == A(713, 713):
		pass
	elif a == A(714, 714):
		pass
	elif a == A(715, 715):
		pass
	elif a == A(716, 716):
		pass
	elif a == A(717, 717):
		pass
	elif a == A(718, 718):
		pass
	elif a == A(719, 719):
		pass
	elif a == A(720, 720):
		pass
	elif a == A(721, 721):
		pass
	elif a == A(722, 722):
		pass
	elif a == A(723, 723):
		pass
	elif a == A(724, 724):
		pass
	elif a == A(725, 725):
		pass
	elif a == A(726, 726):
		pass
	elif a == A(727, 727):
		pass
	elif a == A(728, 728):
		pass
	elif a == A(729, 729):
		pass
	elif a == A(730, 730):
		pass
	elif a == A(731, 731):
		pass
	elif a == A(732, 732):
		pass
	elif a == A(733, 733):
		pass
	elif a == A(734, 734):
		pass
	elif a == A(735, 735):
		pass
	elif a == A(736, 736):
		pass
	elif a == A(737, 737):
		pass
	elif a == A(738, 738):
		pass
	elif a == A(739, 739):
		pass
	elif a == A(740, 740):
		pass
	elif a == A(741, 741):
		pass
	elif a == A(742, 742):
		pass
	elif a == A(743, 743):
		pass
	elif a == A(744, 744):
		pass
	elif a == A(745, 745):
		pass
	elif a == A(746, 746):
		pass
	elif a == A(747, 747):
		pass
	elif a == A(748, 748):
		pass
	elif a == A(749, 749):
		pass
	elif a == A(750, 750):
		pass
	elif a == A(751, 751):
		pass
	elif a == A(752, 752):
		pass
	elif a == A(753, 753):
		pass
	elif a == A(754, 754):
		pass
	elif a == A(755, 755):
		pass
	elif a == A(756, 756):
		pass
	elif a == A(757, 757):
		pass
	elif a == A(758, 758):
		pass
	elif a == A(759, 759):
		pass
	elif a == A(760, 760):
		pass
	elif a == A(761, 761):
		pass
	elif a == A(762, 762):
		pass
	elif a == A(763, 763):
		pass
	elif a == A(764, 764):
		pass
	elif a == A(765, 765):
		pass
	elif a == A(766, 766):
		pass
	elif a == A(767, 767):
		pass
	elif a == A(768, 768):
		pass
	elif a == A(769, 769):
		pass
	elif a == A(770, 770):
		pass
	elif a == A(771, 771):
		pass
	elif a == A(772, 772):
		pass
	elif a == A(773, 773):
		pass
	elif a == A(774, 774):
		pass
	elif a == A(775, 775):
		pass
	elif a == A(776, 776):
		pass
	elif a == A(777, 777):
		pass
	elif a == A(778, 778):
		pass
	elif a == A(779, 779):
		pass
	elif a == A(780, 780):
		pass
	elif a == A(781, 781):
		pass
	elif a == A(782, 782):
		pass
	elif a == A(783, 783):
		pass
	elif a == A(784, 784):
		pass
	elif a == A(785, 785):
		pass
	elif a == A(786, 786):
		pass
	elif a == A(787, 787):
		pass
	elif a == A(788, 788):
		pass
	elif a == A(789, 789):
		pass
	elif a == A(790, 790):
		pass
	elif a == A(791, 791):
		pass
	elif a == A(792, 792):
		pass
	elif a == A(793, 793):
		pass
	elif a == A(794, 794):
		pass
	elif a == A(795, 795):
		pass
	elif a == A(796, 796):
		pass
	elif a == A(797, 797):
		pass
	elif a == A(798, 798):
		pass
	elif a == A(799, 799):
		pass
	elif a == A(800, 800):
		pass
	elif a == A(801, 801):
		pass
	elif a == A(802, 802):
		pass
	elif a == A(803, 803):
		pass
	elif a == A(804, 804):
		pass
	elif a == A(805, 805):
		pass
	elif a == A(806, 806):
		pass
	elif a == A(807, 807):
		pass
	elif a == A(808, 808):
		pass
	elif a == A(809, 809):
		pass
	elif a == A(810, 810):
		pass
	elif a == A(811, 811):
		pass
	elif a == A(812, 812):
		pass
	elif a == A(813, 813):
		pass
	elif a == A(814, 814):
		pass
	elif a == A(815, 815):
		pass
	elif a == A(816, 816):
		pass
	elif a == A(817, 817):
		pass
	elif a == A(818, 818):
		pass
	elif a == A(819, 819):
		pass
	elif a == A(820, 820):
		pass
	elif a == A(821, 821):
		pass
	elif a == A(822, 822):
		pass
	elif a == A(823, 823):
		pass
	elif a == A(824, 824):
		pass
	elif a == A(825, 825):
		pass
	elif a == A(826, 826):
		pass
	elif a == A(827, 827):
		pass
	elif a == A(828, 828):
		pass
	elif a == A(829, 829):
		pass
	elif a == A(830, 830):
		pass
	elif a == A(831, 831):
		pass
	elif a == A(832, 832):
		pass
	elif a == A(833, 833):
		pass
	elif a == A(834, 834):
		pass
	elif a == A(835, 835):
		pass
	elif a == A(836, 836):
		pass
	elif a == A(837, 837):
		pass
	elif a == A(838, 838):
		pass
	elif a == A(839, 839):
		pass
	elif a == A(840, 840):
		pass
	elif a == A(841, 841):
		pass
	elif a == A(842, 842):
		pass
	elif a == A(843, 843):
		pass
	elif a == A(844, 844):
		pass
	elif a == A(845, 845):
		pass
	elif a == A(846, 846):
		pass
	elif a == A(847, 847):
		pass
	elif a == A(848, 848):
		pass
	elif a == A(849, 849):
		pass
	elif a == A(850, 850):
		pass
	elif a == A(851, 851):
		pass
	elif a == A(852, 852):
		pass
	elif a == A(853, 853):
		pass
	elif a == A(854, 854):
		pass
	elif a == A(855, 855):
		pass
	elif a == A(856, 856):
		pass
	elif a == A(857, 857):
		pass
	elif a == A(858, 858):
		pass
	elif a == A(859, 859):
		pass
	elif a == A(860, 860):
		pass
	elif a == A(861, 861):
		pass
	elif a == A(862, 862):
		pass
	elif a == A(863, 863):
		pass
	elif a == A(864, 864):
		pass
	elif a == A(865, 865):
		pass
	elif a == A(866, 866):
		pass
	elif a == A(867, 867):
		pass
	elif a == A(868, 868):
		pass
	elif a == A(869, 869):
		pass
	elif a == A(870, 870):
		pass
	elif a == A(871, 871):
		pass
	elif a == A(872, 872):
		pass
	elif a == A(873, 873):
		pass
	elif a == A(874, 874):
		pass
	elif a == A(875, 875):
		pass
	elif a == A(876, 876):
		pass
	elif a == A(877, 877):
		pass
	elif a == A(878, 878):
		pass
	elif a == A(879, 879):
		pass
	elif a == A(880, 880):
		pass
	elif a == A(881, 881):
		pass
	elif a == A(882, 882):
		pass
	elif a == A(883, 883):
		pass
	elif a == A(884, 884):
		pass
	elif a == A(885, 885):
		pass
	elif a == A(886, 886):
		pass
	elif a == A(887, 887):
		pass
	elif a == A(888, 888):
		pass
	elif a == A(889, 889):
		pass
	elif a == A(890, 890):
		pass
	elif a == A(891, 891):
		pass
	elif a == A(892, 892):
		pass
	elif a == A(893, 893):
		pass
	elif a == A(894, 894):
		pass
	elif a == A(895, 895):
		pass
	elif a == A(896, 896):
		pass
	elif a == A(897, 897):
		pass
	elif a == A(898, 898):
		pass
	elif a == A(899, 899):
		pass
	elif a == A(900, 900):
		pass
	elif a == A(901, 901):
		pass
	elif a == A(902, 902):
		pass
	elif a == A(903, 903):
		pass
	elif a == A(904, 904):
		pass
	elif a == A(905, 905):
		pass
	elif a == A(906, 906):
		pass
	elif a == A(907, 907):
		pass
	elif a == A(908, 908):
		pass
	elif a == A(909, 909):
		pass
	elif a == A(910, 910):
		pass
	elif a == A(911, 911):
		pass
	elif a == A(912, 912):
		pass
	elif a == A(913, 913):
		pass
	elif a == A(914, 914):
		pass
	elif a == A(915, 915):
		pass
	elif a == A(916, 916):
		pass
	elif a == A(917, 917):
		pass
	elif a == A(918, 918):
		pass
	elif a == A(919, 919):
		pass
	elif a == A(920, 920):
		pass
	elif a == A(921, 921):
		pass
	elif a == A(922, 922):
		pass
	elif a == A(923, 923):
		pass
	elif a == A(924, 924):
		pass
	elif a == A(925, 925):
		pass
	elif a == A(926, 926):
		pass
	elif a == A(927, 927):
		pass
	elif a == A(928, 928):
		pass
	elif a == A(929, 929):
		pass
	elif a == A(930, 930):
		pass
	elif a == A(931, 931):
		pass
	elif a == A(932, 932):
		pass
	elif a == A(933, 933):
		pass
	elif a == A(934, 934):
		pass
	elif a == A(935, 935):
		pass
	elif a == A(936, 936):
		pass
	elif a == A(937, 937):
		pass
	elif a == A(938, 938):
		pass
	elif a == A(939, 939):
		pass
	elif a == A(940, 940):
		pass
	elif a == A(941, 941):
		pass
	elif a == A(942, 942):
		pass
	elif a == A(943, 943):
		pass
	elif a == A(944, 944):
		pass
	elif a == A(945, 945):
		pass
	elif a == A(946, 946):
		pass
	elif a == A(947, 947):
		pass
	elif a == A(948, 948):
		pass
	elif a == A(949, 949):
		pass
	elif a == A(950, 950):
		pass
	elif a == A(951, 951):
		pass
	elif a == A(952, 952):
		pass
	elif a == A(953, 953):
		pass
	elif a == A(954, 954):
		pass
	elif a == A(955, 955):
		pass
	elif a == A(956, 956):
		pass
	elif a == A(957, 957):
		pass
	elif a == A(958, 958):
		pass
	elif a == A(959, 959):
		pass
	elif a == A(960, 960):
		pass
	elif a == A(961, 961):
		pass
	elif a == A(962, 962):
		pass
	elif a == A(963, 963):
		pass
	elif a == A(964, 964):
		pass
	elif a == A(965, 965):
		pass
	elif a == A(966, 966):
		pass
	elif a == A(967, 967):
		pass
	elif a == A(968, 968):
		pass
	elif a == A(969, 969):
		pass
	elif a == A(970, 970):
		pass
	elif a == A(971, 971):
		pass
	elif a == A(972, 972):
		pass
	elif a == A(973, 973):
		pass
	elif a == A(974, 974):
		pass
	elif a == A(975, 975):
		pass
	elif a == A(976, 976):
		pass
	elif a == A(977, 977):
		pass
	elif a == A(978, 978):
		pass
	elif a == A(979, 979):
		pass
	elif a == A(980, 980):
		pass
	elif a == A(981, 981):
		pass
	elif a == A(982, 982):
		pass
	elif a == A(983, 983):
		pass
	elif a == A(984, 984):
		pass
	elif a == A(985, 985):
		pass
	elif a == A(986, 986):
		pass
	elif a == A(987, 987):
		pass
	elif a == A(988, 988):
		pass
	elif a == A(989, 989):
		pass
	elif a == A(990, 990):
		pass
	elif a == A(991, 991):
		pass
	elif a == A(992, 992):
		pass
	elif a == A(993, 993):
		pass
	elif a == A(994, 994):
		pass
	elif a == A(995, 995):
		pass
	elif a == A(996, 996):
		pass
	elif a == A(997, 997):
		pass
	elif a == A(998, 998):
		pass
	elif a == A(999, 999):
		pass


print(timeit.timeit(foo))  # 426.9204228409799


# for i in range(1000):
# 	print(f"\telif a == A({i}, {i}):\n\t\tpass")
