import timeit
from dataclasses import dataclass


@dataclass()
class A:
	a: int
	b: int


a = A(999,999)


def foo():
	match a:
		case A(0, 0):
			pass
		case A(1, 1):
			pass
		case A(2, 2):
			pass
		case A(3, 3):
			pass
		case A(4, 4):
			pass
		case A(5, 5):
			pass
		case A(6, 6):
			pass
		case A(7, 7):
			pass
		case A(8, 8):
			pass
		case A(9, 9):
			pass
		case A(10, 10):
			pass
		case A(11, 11):
			pass
		case A(12, 12):
			pass
		case A(13, 13):
			pass
		case A(14, 14):
			pass
		case A(15, 15):
			pass
		case A(16, 16):
			pass
		case A(17, 17):
			pass
		case A(18, 18):
			pass
		case A(19, 19):
			pass
		case A(20, 20):
			pass
		case A(21, 21):
			pass
		case A(22, 22):
			pass
		case A(23, 23):
			pass
		case A(24, 24):
			pass
		case A(25, 25):
			pass
		case A(26, 26):
			pass
		case A(27, 27):
			pass
		case A(28, 28):
			pass
		case A(29, 29):
			pass
		case A(30, 30):
			pass
		case A(31, 31):
			pass
		case A(32, 32):
			pass
		case A(33, 33):
			pass
		case A(34, 34):
			pass
		case A(35, 35):
			pass
		case A(36, 36):
			pass
		case A(37, 37):
			pass
		case A(38, 38):
			pass
		case A(39, 39):
			pass
		case A(40, 40):
			pass
		case A(41, 41):
			pass
		case A(42, 42):
			pass
		case A(43, 43):
			pass
		case A(44, 44):
			pass
		case A(45, 45):
			pass
		case A(46, 46):
			pass
		case A(47, 47):
			pass
		case A(48, 48):
			pass
		case A(49, 49):
			pass
		case A(50, 50):
			pass
		case A(51, 51):
			pass
		case A(52, 52):
			pass
		case A(53, 53):
			pass
		case A(54, 54):
			pass
		case A(55, 55):
			pass
		case A(56, 56):
			pass
		case A(57, 57):
			pass
		case A(58, 58):
			pass
		case A(59, 59):
			pass
		case A(60, 60):
			pass
		case A(61, 61):
			pass
		case A(62, 62):
			pass
		case A(63, 63):
			pass
		case A(64, 64):
			pass
		case A(65, 65):
			pass
		case A(66, 66):
			pass
		case A(67, 67):
			pass
		case A(68, 68):
			pass
		case A(69, 69):
			pass
		case A(70, 70):
			pass
		case A(71, 71):
			pass
		case A(72, 72):
			pass
		case A(73, 73):
			pass
		case A(74, 74):
			pass
		case A(75, 75):
			pass
		case A(76, 76):
			pass
		case A(77, 77):
			pass
		case A(78, 78):
			pass
		case A(79, 79):
			pass
		case A(80, 80):
			pass
		case A(81, 81):
			pass
		case A(82, 82):
			pass
		case A(83, 83):
			pass
		case A(84, 84):
			pass
		case A(85, 85):
			pass
		case A(86, 86):
			pass
		case A(87, 87):
			pass
		case A(88, 88):
			pass
		case A(89, 89):
			pass
		case A(90, 90):
			pass
		case A(91, 91):
			pass
		case A(92, 92):
			pass
		case A(93, 93):
			pass
		case A(94, 94):
			pass
		case A(95, 95):
			pass
		case A(96, 96):
			pass
		case A(97, 97):
			pass
		case A(98, 98):
			pass
		case A(99, 99):
			pass
		case A(100, 100):
			pass
		case A(101, 101):
			pass
		case A(102, 102):
			pass
		case A(103, 103):
			pass
		case A(104, 104):
			pass
		case A(105, 105):
			pass
		case A(106, 106):
			pass
		case A(107, 107):
			pass
		case A(108, 108):
			pass
		case A(109, 109):
			pass
		case A(110, 110):
			pass
		case A(111, 111):
			pass
		case A(112, 112):
			pass
		case A(113, 113):
			pass
		case A(114, 114):
			pass
		case A(115, 115):
			pass
		case A(116, 116):
			pass
		case A(117, 117):
			pass
		case A(118, 118):
			pass
		case A(119, 119):
			pass
		case A(120, 120):
			pass
		case A(121, 121):
			pass
		case A(122, 122):
			pass
		case A(123, 123):
			pass
		case A(124, 124):
			pass
		case A(125, 125):
			pass
		case A(126, 126):
			pass
		case A(127, 127):
			pass
		case A(128, 128):
			pass
		case A(129, 129):
			pass
		case A(130, 130):
			pass
		case A(131, 131):
			pass
		case A(132, 132):
			pass
		case A(133, 133):
			pass
		case A(134, 134):
			pass
		case A(135, 135):
			pass
		case A(136, 136):
			pass
		case A(137, 137):
			pass
		case A(138, 138):
			pass
		case A(139, 139):
			pass
		case A(140, 140):
			pass
		case A(141, 141):
			pass
		case A(142, 142):
			pass
		case A(143, 143):
			pass
		case A(144, 144):
			pass
		case A(145, 145):
			pass
		case A(146, 146):
			pass
		case A(147, 147):
			pass
		case A(148, 148):
			pass
		case A(149, 149):
			pass
		case A(150, 150):
			pass
		case A(151, 151):
			pass
		case A(152, 152):
			pass
		case A(153, 153):
			pass
		case A(154, 154):
			pass
		case A(155, 155):
			pass
		case A(156, 156):
			pass
		case A(157, 157):
			pass
		case A(158, 158):
			pass
		case A(159, 159):
			pass
		case A(160, 160):
			pass
		case A(161, 161):
			pass
		case A(162, 162):
			pass
		case A(163, 163):
			pass
		case A(164, 164):
			pass
		case A(165, 165):
			pass
		case A(166, 166):
			pass
		case A(167, 167):
			pass
		case A(168, 168):
			pass
		case A(169, 169):
			pass
		case A(170, 170):
			pass
		case A(171, 171):
			pass
		case A(172, 172):
			pass
		case A(173, 173):
			pass
		case A(174, 174):
			pass
		case A(175, 175):
			pass
		case A(176, 176):
			pass
		case A(177, 177):
			pass
		case A(178, 178):
			pass
		case A(179, 179):
			pass
		case A(180, 180):
			pass
		case A(181, 181):
			pass
		case A(182, 182):
			pass
		case A(183, 183):
			pass
		case A(184, 184):
			pass
		case A(185, 185):
			pass
		case A(186, 186):
			pass
		case A(187, 187):
			pass
		case A(188, 188):
			pass
		case A(189, 189):
			pass
		case A(190, 190):
			pass
		case A(191, 191):
			pass
		case A(192, 192):
			pass
		case A(193, 193):
			pass
		case A(194, 194):
			pass
		case A(195, 195):
			pass
		case A(196, 196):
			pass
		case A(197, 197):
			pass
		case A(198, 198):
			pass
		case A(199, 199):
			pass
		case A(200, 200):
			pass
		case A(201, 201):
			pass
		case A(202, 202):
			pass
		case A(203, 203):
			pass
		case A(204, 204):
			pass
		case A(205, 205):
			pass
		case A(206, 206):
			pass
		case A(207, 207):
			pass
		case A(208, 208):
			pass
		case A(209, 209):
			pass
		case A(210, 210):
			pass
		case A(211, 211):
			pass
		case A(212, 212):
			pass
		case A(213, 213):
			pass
		case A(214, 214):
			pass
		case A(215, 215):
			pass
		case A(216, 216):
			pass
		case A(217, 217):
			pass
		case A(218, 218):
			pass
		case A(219, 219):
			pass
		case A(220, 220):
			pass
		case A(221, 221):
			pass
		case A(222, 222):
			pass
		case A(223, 223):
			pass
		case A(224, 224):
			pass
		case A(225, 225):
			pass
		case A(226, 226):
			pass
		case A(227, 227):
			pass
		case A(228, 228):
			pass
		case A(229, 229):
			pass
		case A(230, 230):
			pass
		case A(231, 231):
			pass
		case A(232, 232):
			pass
		case A(233, 233):
			pass
		case A(234, 234):
			pass
		case A(235, 235):
			pass
		case A(236, 236):
			pass
		case A(237, 237):
			pass
		case A(238, 238):
			pass
		case A(239, 239):
			pass
		case A(240, 240):
			pass
		case A(241, 241):
			pass
		case A(242, 242):
			pass
		case A(243, 243):
			pass
		case A(244, 244):
			pass
		case A(245, 245):
			pass
		case A(246, 246):
			pass
		case A(247, 247):
			pass
		case A(248, 248):
			pass
		case A(249, 249):
			pass
		case A(250, 250):
			pass
		case A(251, 251):
			pass
		case A(252, 252):
			pass
		case A(253, 253):
			pass
		case A(254, 254):
			pass
		case A(255, 255):
			pass
		case A(256, 256):
			pass
		case A(257, 257):
			pass
		case A(258, 258):
			pass
		case A(259, 259):
			pass
		case A(260, 260):
			pass
		case A(261, 261):
			pass
		case A(262, 262):
			pass
		case A(263, 263):
			pass
		case A(264, 264):
			pass
		case A(265, 265):
			pass
		case A(266, 266):
			pass
		case A(267, 267):
			pass
		case A(268, 268):
			pass
		case A(269, 269):
			pass
		case A(270, 270):
			pass
		case A(271, 271):
			pass
		case A(272, 272):
			pass
		case A(273, 273):
			pass
		case A(274, 274):
			pass
		case A(275, 275):
			pass
		case A(276, 276):
			pass
		case A(277, 277):
			pass
		case A(278, 278):
			pass
		case A(279, 279):
			pass
		case A(280, 280):
			pass
		case A(281, 281):
			pass
		case A(282, 282):
			pass
		case A(283, 283):
			pass
		case A(284, 284):
			pass
		case A(285, 285):
			pass
		case A(286, 286):
			pass
		case A(287, 287):
			pass
		case A(288, 288):
			pass
		case A(289, 289):
			pass
		case A(290, 290):
			pass
		case A(291, 291):
			pass
		case A(292, 292):
			pass
		case A(293, 293):
			pass
		case A(294, 294):
			pass
		case A(295, 295):
			pass
		case A(296, 296):
			pass
		case A(297, 297):
			pass
		case A(298, 298):
			pass
		case A(299, 299):
			pass
		case A(300, 300):
			pass
		case A(301, 301):
			pass
		case A(302, 302):
			pass
		case A(303, 303):
			pass
		case A(304, 304):
			pass
		case A(305, 305):
			pass
		case A(306, 306):
			pass
		case A(307, 307):
			pass
		case A(308, 308):
			pass
		case A(309, 309):
			pass
		case A(310, 310):
			pass
		case A(311, 311):
			pass
		case A(312, 312):
			pass
		case A(313, 313):
			pass
		case A(314, 314):
			pass
		case A(315, 315):
			pass
		case A(316, 316):
			pass
		case A(317, 317):
			pass
		case A(318, 318):
			pass
		case A(319, 319):
			pass
		case A(320, 320):
			pass
		case A(321, 321):
			pass
		case A(322, 322):
			pass
		case A(323, 323):
			pass
		case A(324, 324):
			pass
		case A(325, 325):
			pass
		case A(326, 326):
			pass
		case A(327, 327):
			pass
		case A(328, 328):
			pass
		case A(329, 329):
			pass
		case A(330, 330):
			pass
		case A(331, 331):
			pass
		case A(332, 332):
			pass
		case A(333, 333):
			pass
		case A(334, 334):
			pass
		case A(335, 335):
			pass
		case A(336, 336):
			pass
		case A(337, 337):
			pass
		case A(338, 338):
			pass
		case A(339, 339):
			pass
		case A(340, 340):
			pass
		case A(341, 341):
			pass
		case A(342, 342):
			pass
		case A(343, 343):
			pass
		case A(344, 344):
			pass
		case A(345, 345):
			pass
		case A(346, 346):
			pass
		case A(347, 347):
			pass
		case A(348, 348):
			pass
		case A(349, 349):
			pass
		case A(350, 350):
			pass
		case A(351, 351):
			pass
		case A(352, 352):
			pass
		case A(353, 353):
			pass
		case A(354, 354):
			pass
		case A(355, 355):
			pass
		case A(356, 356):
			pass
		case A(357, 357):
			pass
		case A(358, 358):
			pass
		case A(359, 359):
			pass
		case A(360, 360):
			pass
		case A(361, 361):
			pass
		case A(362, 362):
			pass
		case A(363, 363):
			pass
		case A(364, 364):
			pass
		case A(365, 365):
			pass
		case A(366, 366):
			pass
		case A(367, 367):
			pass
		case A(368, 368):
			pass
		case A(369, 369):
			pass
		case A(370, 370):
			pass
		case A(371, 371):
			pass
		case A(372, 372):
			pass
		case A(373, 373):
			pass
		case A(374, 374):
			pass
		case A(375, 375):
			pass
		case A(376, 376):
			pass
		case A(377, 377):
			pass
		case A(378, 378):
			pass
		case A(379, 379):
			pass
		case A(380, 380):
			pass
		case A(381, 381):
			pass
		case A(382, 382):
			pass
		case A(383, 383):
			pass
		case A(384, 384):
			pass
		case A(385, 385):
			pass
		case A(386, 386):
			pass
		case A(387, 387):
			pass
		case A(388, 388):
			pass
		case A(389, 389):
			pass
		case A(390, 390):
			pass
		case A(391, 391):
			pass
		case A(392, 392):
			pass
		case A(393, 393):
			pass
		case A(394, 394):
			pass
		case A(395, 395):
			pass
		case A(396, 396):
			pass
		case A(397, 397):
			pass
		case A(398, 398):
			pass
		case A(399, 399):
			pass
		case A(400, 400):
			pass
		case A(401, 401):
			pass
		case A(402, 402):
			pass
		case A(403, 403):
			pass
		case A(404, 404):
			pass
		case A(405, 405):
			pass
		case A(406, 406):
			pass
		case A(407, 407):
			pass
		case A(408, 408):
			pass
		case A(409, 409):
			pass
		case A(410, 410):
			pass
		case A(411, 411):
			pass
		case A(412, 412):
			pass
		case A(413, 413):
			pass
		case A(414, 414):
			pass
		case A(415, 415):
			pass
		case A(416, 416):
			pass
		case A(417, 417):
			pass
		case A(418, 418):
			pass
		case A(419, 419):
			pass
		case A(420, 420):
			pass
		case A(421, 421):
			pass
		case A(422, 422):
			pass
		case A(423, 423):
			pass
		case A(424, 424):
			pass
		case A(425, 425):
			pass
		case A(426, 426):
			pass
		case A(427, 427):
			pass
		case A(428, 428):
			pass
		case A(429, 429):
			pass
		case A(430, 430):
			pass
		case A(431, 431):
			pass
		case A(432, 432):
			pass
		case A(433, 433):
			pass
		case A(434, 434):
			pass
		case A(435, 435):
			pass
		case A(436, 436):
			pass
		case A(437, 437):
			pass
		case A(438, 438):
			pass
		case A(439, 439):
			pass
		case A(440, 440):
			pass
		case A(441, 441):
			pass
		case A(442, 442):
			pass
		case A(443, 443):
			pass
		case A(444, 444):
			pass
		case A(445, 445):
			pass
		case A(446, 446):
			pass
		case A(447, 447):
			pass
		case A(448, 448):
			pass
		case A(449, 449):
			pass
		case A(450, 450):
			pass
		case A(451, 451):
			pass
		case A(452, 452):
			pass
		case A(453, 453):
			pass
		case A(454, 454):
			pass
		case A(455, 455):
			pass
		case A(456, 456):
			pass
		case A(457, 457):
			pass
		case A(458, 458):
			pass
		case A(459, 459):
			pass
		case A(460, 460):
			pass
		case A(461, 461):
			pass
		case A(462, 462):
			pass
		case A(463, 463):
			pass
		case A(464, 464):
			pass
		case A(465, 465):
			pass
		case A(466, 466):
			pass
		case A(467, 467):
			pass
		case A(468, 468):
			pass
		case A(469, 469):
			pass
		case A(470, 470):
			pass
		case A(471, 471):
			pass
		case A(472, 472):
			pass
		case A(473, 473):
			pass
		case A(474, 474):
			pass
		case A(475, 475):
			pass
		case A(476, 476):
			pass
		case A(477, 477):
			pass
		case A(478, 478):
			pass
		case A(479, 479):
			pass
		case A(480, 480):
			pass
		case A(481, 481):
			pass
		case A(482, 482):
			pass
		case A(483, 483):
			pass
		case A(484, 484):
			pass
		case A(485, 485):
			pass
		case A(486, 486):
			pass
		case A(487, 487):
			pass
		case A(488, 488):
			pass
		case A(489, 489):
			pass
		case A(490, 490):
			pass
		case A(491, 491):
			pass
		case A(492, 492):
			pass
		case A(493, 493):
			pass
		case A(494, 494):
			pass
		case A(495, 495):
			pass
		case A(496, 496):
			pass
		case A(497, 497):
			pass
		case A(498, 498):
			pass
		case A(499, 499):
			pass
		case A(500, 500):
			pass
		case A(501, 501):
			pass
		case A(502, 502):
			pass
		case A(503, 503):
			pass
		case A(504, 504):
			pass
		case A(505, 505):
			pass
		case A(506, 506):
			pass
		case A(507, 507):
			pass
		case A(508, 508):
			pass
		case A(509, 509):
			pass
		case A(510, 510):
			pass
		case A(511, 511):
			pass
		case A(512, 512):
			pass
		case A(513, 513):
			pass
		case A(514, 514):
			pass
		case A(515, 515):
			pass
		case A(516, 516):
			pass
		case A(517, 517):
			pass
		case A(518, 518):
			pass
		case A(519, 519):
			pass
		case A(520, 520):
			pass
		case A(521, 521):
			pass
		case A(522, 522):
			pass
		case A(523, 523):
			pass
		case A(524, 524):
			pass
		case A(525, 525):
			pass
		case A(526, 526):
			pass
		case A(527, 527):
			pass
		case A(528, 528):
			pass
		case A(529, 529):
			pass
		case A(530, 530):
			pass
		case A(531, 531):
			pass
		case A(532, 532):
			pass
		case A(533, 533):
			pass
		case A(534, 534):
			pass
		case A(535, 535):
			pass
		case A(536, 536):
			pass
		case A(537, 537):
			pass
		case A(538, 538):
			pass
		case A(539, 539):
			pass
		case A(540, 540):
			pass
		case A(541, 541):
			pass
		case A(542, 542):
			pass
		case A(543, 543):
			pass
		case A(544, 544):
			pass
		case A(545, 545):
			pass
		case A(546, 546):
			pass
		case A(547, 547):
			pass
		case A(548, 548):
			pass
		case A(549, 549):
			pass
		case A(550, 550):
			pass
		case A(551, 551):
			pass
		case A(552, 552):
			pass
		case A(553, 553):
			pass
		case A(554, 554):
			pass
		case A(555, 555):
			pass
		case A(556, 556):
			pass
		case A(557, 557):
			pass
		case A(558, 558):
			pass
		case A(559, 559):
			pass
		case A(560, 560):
			pass
		case A(561, 561):
			pass
		case A(562, 562):
			pass
		case A(563, 563):
			pass
		case A(564, 564):
			pass
		case A(565, 565):
			pass
		case A(566, 566):
			pass
		case A(567, 567):
			pass
		case A(568, 568):
			pass
		case A(569, 569):
			pass
		case A(570, 570):
			pass
		case A(571, 571):
			pass
		case A(572, 572):
			pass
		case A(573, 573):
			pass
		case A(574, 574):
			pass
		case A(575, 575):
			pass
		case A(576, 576):
			pass
		case A(577, 577):
			pass
		case A(578, 578):
			pass
		case A(579, 579):
			pass
		case A(580, 580):
			pass
		case A(581, 581):
			pass
		case A(582, 582):
			pass
		case A(583, 583):
			pass
		case A(584, 584):
			pass
		case A(585, 585):
			pass
		case A(586, 586):
			pass
		case A(587, 587):
			pass
		case A(588, 588):
			pass
		case A(589, 589):
			pass
		case A(590, 590):
			pass
		case A(591, 591):
			pass
		case A(592, 592):
			pass
		case A(593, 593):
			pass
		case A(594, 594):
			pass
		case A(595, 595):
			pass
		case A(596, 596):
			pass
		case A(597, 597):
			pass
		case A(598, 598):
			pass
		case A(599, 599):
			pass
		case A(600, 600):
			pass
		case A(601, 601):
			pass
		case A(602, 602):
			pass
		case A(603, 603):
			pass
		case A(604, 604):
			pass
		case A(605, 605):
			pass
		case A(606, 606):
			pass
		case A(607, 607):
			pass
		case A(608, 608):
			pass
		case A(609, 609):
			pass
		case A(610, 610):
			pass
		case A(611, 611):
			pass
		case A(612, 612):
			pass
		case A(613, 613):
			pass
		case A(614, 614):
			pass
		case A(615, 615):
			pass
		case A(616, 616):
			pass
		case A(617, 617):
			pass
		case A(618, 618):
			pass
		case A(619, 619):
			pass
		case A(620, 620):
			pass
		case A(621, 621):
			pass
		case A(622, 622):
			pass
		case A(623, 623):
			pass
		case A(624, 624):
			pass
		case A(625, 625):
			pass
		case A(626, 626):
			pass
		case A(627, 627):
			pass
		case A(628, 628):
			pass
		case A(629, 629):
			pass
		case A(630, 630):
			pass
		case A(631, 631):
			pass
		case A(632, 632):
			pass
		case A(633, 633):
			pass
		case A(634, 634):
			pass
		case A(635, 635):
			pass
		case A(636, 636):
			pass
		case A(637, 637):
			pass
		case A(638, 638):
			pass
		case A(639, 639):
			pass
		case A(640, 640):
			pass
		case A(641, 641):
			pass
		case A(642, 642):
			pass
		case A(643, 643):
			pass
		case A(644, 644):
			pass
		case A(645, 645):
			pass
		case A(646, 646):
			pass
		case A(647, 647):
			pass
		case A(648, 648):
			pass
		case A(649, 649):
			pass
		case A(650, 650):
			pass
		case A(651, 651):
			pass
		case A(652, 652):
			pass
		case A(653, 653):
			pass
		case A(654, 654):
			pass
		case A(655, 655):
			pass
		case A(656, 656):
			pass
		case A(657, 657):
			pass
		case A(658, 658):
			pass
		case A(659, 659):
			pass
		case A(660, 660):
			pass
		case A(661, 661):
			pass
		case A(662, 662):
			pass
		case A(663, 663):
			pass
		case A(664, 664):
			pass
		case A(665, 665):
			pass
		case A(666, 666):
			pass
		case A(667, 667):
			pass
		case A(668, 668):
			pass
		case A(669, 669):
			pass
		case A(670, 670):
			pass
		case A(671, 671):
			pass
		case A(672, 672):
			pass
		case A(673, 673):
			pass
		case A(674, 674):
			pass
		case A(675, 675):
			pass
		case A(676, 676):
			pass
		case A(677, 677):
			pass
		case A(678, 678):
			pass
		case A(679, 679):
			pass
		case A(680, 680):
			pass
		case A(681, 681):
			pass
		case A(682, 682):
			pass
		case A(683, 683):
			pass
		case A(684, 684):
			pass
		case A(685, 685):
			pass
		case A(686, 686):
			pass
		case A(687, 687):
			pass
		case A(688, 688):
			pass
		case A(689, 689):
			pass
		case A(690, 690):
			pass
		case A(691, 691):
			pass
		case A(692, 692):
			pass
		case A(693, 693):
			pass
		case A(694, 694):
			pass
		case A(695, 695):
			pass
		case A(696, 696):
			pass
		case A(697, 697):
			pass
		case A(698, 698):
			pass
		case A(699, 699):
			pass
		case A(700, 700):
			pass
		case A(701, 701):
			pass
		case A(702, 702):
			pass
		case A(703, 703):
			pass
		case A(704, 704):
			pass
		case A(705, 705):
			pass
		case A(706, 706):
			pass
		case A(707, 707):
			pass
		case A(708, 708):
			pass
		case A(709, 709):
			pass
		case A(710, 710):
			pass
		case A(711, 711):
			pass
		case A(712, 712):
			pass
		case A(713, 713):
			pass
		case A(714, 714):
			pass
		case A(715, 715):
			pass
		case A(716, 716):
			pass
		case A(717, 717):
			pass
		case A(718, 718):
			pass
		case A(719, 719):
			pass
		case A(720, 720):
			pass
		case A(721, 721):
			pass
		case A(722, 722):
			pass
		case A(723, 723):
			pass
		case A(724, 724):
			pass
		case A(725, 725):
			pass
		case A(726, 726):
			pass
		case A(727, 727):
			pass
		case A(728, 728):
			pass
		case A(729, 729):
			pass
		case A(730, 730):
			pass
		case A(731, 731):
			pass
		case A(732, 732):
			pass
		case A(733, 733):
			pass
		case A(734, 734):
			pass
		case A(735, 735):
			pass
		case A(736, 736):
			pass
		case A(737, 737):
			pass
		case A(738, 738):
			pass
		case A(739, 739):
			pass
		case A(740, 740):
			pass
		case A(741, 741):
			pass
		case A(742, 742):
			pass
		case A(743, 743):
			pass
		case A(744, 744):
			pass
		case A(745, 745):
			pass
		case A(746, 746):
			pass
		case A(747, 747):
			pass
		case A(748, 748):
			pass
		case A(749, 749):
			pass
		case A(750, 750):
			pass
		case A(751, 751):
			pass
		case A(752, 752):
			pass
		case A(753, 753):
			pass
		case A(754, 754):
			pass
		case A(755, 755):
			pass
		case A(756, 756):
			pass
		case A(757, 757):
			pass
		case A(758, 758):
			pass
		case A(759, 759):
			pass
		case A(760, 760):
			pass
		case A(761, 761):
			pass
		case A(762, 762):
			pass
		case A(763, 763):
			pass
		case A(764, 764):
			pass
		case A(765, 765):
			pass
		case A(766, 766):
			pass
		case A(767, 767):
			pass
		case A(768, 768):
			pass
		case A(769, 769):
			pass
		case A(770, 770):
			pass
		case A(771, 771):
			pass
		case A(772, 772):
			pass
		case A(773, 773):
			pass
		case A(774, 774):
			pass
		case A(775, 775):
			pass
		case A(776, 776):
			pass
		case A(777, 777):
			pass
		case A(778, 778):
			pass
		case A(779, 779):
			pass
		case A(780, 780):
			pass
		case A(781, 781):
			pass
		case A(782, 782):
			pass
		case A(783, 783):
			pass
		case A(784, 784):
			pass
		case A(785, 785):
			pass
		case A(786, 786):
			pass
		case A(787, 787):
			pass
		case A(788, 788):
			pass
		case A(789, 789):
			pass
		case A(790, 790):
			pass
		case A(791, 791):
			pass
		case A(792, 792):
			pass
		case A(793, 793):
			pass
		case A(794, 794):
			pass
		case A(795, 795):
			pass
		case A(796, 796):
			pass
		case A(797, 797):
			pass
		case A(798, 798):
			pass
		case A(799, 799):
			pass
		case A(800, 800):
			pass
		case A(801, 801):
			pass
		case A(802, 802):
			pass
		case A(803, 803):
			pass
		case A(804, 804):
			pass
		case A(805, 805):
			pass
		case A(806, 806):
			pass
		case A(807, 807):
			pass
		case A(808, 808):
			pass
		case A(809, 809):
			pass
		case A(810, 810):
			pass
		case A(811, 811):
			pass
		case A(812, 812):
			pass
		case A(813, 813):
			pass
		case A(814, 814):
			pass
		case A(815, 815):
			pass
		case A(816, 816):
			pass
		case A(817, 817):
			pass
		case A(818, 818):
			pass
		case A(819, 819):
			pass
		case A(820, 820):
			pass
		case A(821, 821):
			pass
		case A(822, 822):
			pass
		case A(823, 823):
			pass
		case A(824, 824):
			pass
		case A(825, 825):
			pass
		case A(826, 826):
			pass
		case A(827, 827):
			pass
		case A(828, 828):
			pass
		case A(829, 829):
			pass
		case A(830, 830):
			pass
		case A(831, 831):
			pass
		case A(832, 832):
			pass
		case A(833, 833):
			pass
		case A(834, 834):
			pass
		case A(835, 835):
			pass
		case A(836, 836):
			pass
		case A(837, 837):
			pass
		case A(838, 838):
			pass
		case A(839, 839):
			pass
		case A(840, 840):
			pass
		case A(841, 841):
			pass
		case A(842, 842):
			pass
		case A(843, 843):
			pass
		case A(844, 844):
			pass
		case A(845, 845):
			pass
		case A(846, 846):
			pass
		case A(847, 847):
			pass
		case A(848, 848):
			pass
		case A(849, 849):
			pass
		case A(850, 850):
			pass
		case A(851, 851):
			pass
		case A(852, 852):
			pass
		case A(853, 853):
			pass
		case A(854, 854):
			pass
		case A(855, 855):
			pass
		case A(856, 856):
			pass
		case A(857, 857):
			pass
		case A(858, 858):
			pass
		case A(859, 859):
			pass
		case A(860, 860):
			pass
		case A(861, 861):
			pass
		case A(862, 862):
			pass
		case A(863, 863):
			pass
		case A(864, 864):
			pass
		case A(865, 865):
			pass
		case A(866, 866):
			pass
		case A(867, 867):
			pass
		case A(868, 868):
			pass
		case A(869, 869):
			pass
		case A(870, 870):
			pass
		case A(871, 871):
			pass
		case A(872, 872):
			pass
		case A(873, 873):
			pass
		case A(874, 874):
			pass
		case A(875, 875):
			pass
		case A(876, 876):
			pass
		case A(877, 877):
			pass
		case A(878, 878):
			pass
		case A(879, 879):
			pass
		case A(880, 880):
			pass
		case A(881, 881):
			pass
		case A(882, 882):
			pass
		case A(883, 883):
			pass
		case A(884, 884):
			pass
		case A(885, 885):
			pass
		case A(886, 886):
			pass
		case A(887, 887):
			pass
		case A(888, 888):
			pass
		case A(889, 889):
			pass
		case A(890, 890):
			pass
		case A(891, 891):
			pass
		case A(892, 892):
			pass
		case A(893, 893):
			pass
		case A(894, 894):
			pass
		case A(895, 895):
			pass
		case A(896, 896):
			pass
		case A(897, 897):
			pass
		case A(898, 898):
			pass
		case A(899, 899):
			pass
		case A(900, 900):
			pass
		case A(901, 901):
			pass
		case A(902, 902):
			pass
		case A(903, 903):
			pass
		case A(904, 904):
			pass
		case A(905, 905):
			pass
		case A(906, 906):
			pass
		case A(907, 907):
			pass
		case A(908, 908):
			pass
		case A(909, 909):
			pass
		case A(910, 910):
			pass
		case A(911, 911):
			pass
		case A(912, 912):
			pass
		case A(913, 913):
			pass
		case A(914, 914):
			pass
		case A(915, 915):
			pass
		case A(916, 916):
			pass
		case A(917, 917):
			pass
		case A(918, 918):
			pass
		case A(919, 919):
			pass
		case A(920, 920):
			pass
		case A(921, 921):
			pass
		case A(922, 922):
			pass
		case A(923, 923):
			pass
		case A(924, 924):
			pass
		case A(925, 925):
			pass
		case A(926, 926):
			pass
		case A(927, 927):
			pass
		case A(928, 928):
			pass
		case A(929, 929):
			pass
		case A(930, 930):
			pass
		case A(931, 931):
			pass
		case A(932, 932):
			pass
		case A(933, 933):
			pass
		case A(934, 934):
			pass
		case A(935, 935):
			pass
		case A(936, 936):
			pass
		case A(937, 937):
			pass
		case A(938, 938):
			pass
		case A(939, 939):
			pass
		case A(940, 940):
			pass
		case A(941, 941):
			pass
		case A(942, 942):
			pass
		case A(943, 943):
			pass
		case A(944, 944):
			pass
		case A(945, 945):
			pass
		case A(946, 946):
			pass
		case A(947, 947):
			pass
		case A(948, 948):
			pass
		case A(949, 949):
			pass
		case A(950, 950):
			pass
		case A(951, 951):
			pass
		case A(952, 952):
			pass
		case A(953, 953):
			pass
		case A(954, 954):
			pass
		case A(955, 955):
			pass
		case A(956, 956):
			pass
		case A(957, 957):
			pass
		case A(958, 958):
			pass
		case A(959, 959):
			pass
		case A(960, 960):
			pass
		case A(961, 961):
			pass
		case A(962, 962):
			pass
		case A(963, 963):
			pass
		case A(964, 964):
			pass
		case A(965, 965):
			pass
		case A(966, 966):
			pass
		case A(967, 967):
			pass
		case A(968, 968):
			pass
		case A(969, 969):
			pass
		case A(970, 970):
			pass
		case A(971, 971):
			pass
		case A(972, 972):
			pass
		case A(973, 973):
			pass
		case A(974, 974):
			pass
		case A(975, 975):
			pass
		case A(976, 976):
			pass
		case A(977, 977):
			pass
		case A(978, 978):
			pass
		case A(979, 979):
			pass
		case A(980, 980):
			pass
		case A(981, 981):
			pass
		case A(982, 982):
			pass
		case A(983, 983):
			pass
		case A(984, 984):
			pass
		case A(985, 985):
			pass
		case A(986, 986):
			pass
		case A(987, 987):
			pass
		case A(988, 988):
			pass
		case A(989, 989):
			pass
		case A(990, 990):
			pass
		case A(991, 991):
			pass
		case A(992, 992):
			pass
		case A(993, 993):
			pass
		case A(994, 994):
			pass
		case A(995, 995):
			pass
		case A(996, 996):
			pass
		case A(997, 997):
			pass
		case A(998, 998):
			pass
		case A(999, 999):
			pass


print(timeit.timeit(foo))  # 397.5815292279585

# for i in range(1000):
# 	print(f"\t\tcase A({i}, {i}):\n\t\t\tpass")
