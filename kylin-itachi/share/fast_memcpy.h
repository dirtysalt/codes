/*
 * Copyright (C) dirlt
 */

#ifndef __CC_SHARE_FAST_MEMCPY_H__
#define __CC_SHARE_FAST_MEMCPY_H__

#include <stdint.h>
#include <cstring>

namespace share {

template<const size_t N>
static inline void _fast_memcpy(void* dst, const void* src) {
    struct X {
        uint8_t byte[N];
    };
    *(reinterpret_cast<X*>(dst)) = *(reinterpret_cast<const X*>(src));
}

template<>
inline void _fast_memcpy<0>(void*, const void*) {
}

static inline void fast_memcpy(void* dst, const void* src, size_t size) {
    if (size <= 16) {
        if (size == 0)  return ;
        if (size == 1)  return _fast_memcpy<1>(dst, src);
        if (size == 2)  return _fast_memcpy<2>(dst, src);
        if (size == 3)  return _fast_memcpy<3>(dst, src);
        if (size == 4)  return _fast_memcpy<4>(dst, src);
        if (size == 5)  return _fast_memcpy<5>(dst, src);
        if (size == 6)  return _fast_memcpy<6>(dst, src);
        if (size == 7)  return _fast_memcpy<7>(dst, src);
        if (size == 8)  return _fast_memcpy<8>(dst, src);
        if (size == 9)  return _fast_memcpy<9>(dst, src);
        if (size == 10) return _fast_memcpy<10>(dst, src);
        if (size == 11) return _fast_memcpy<11>(dst, src);
        if (size == 12) return _fast_memcpy<12>(dst, src);
        if (size == 13) return _fast_memcpy<13>(dst, src);
        if (size == 14) return _fast_memcpy<14>(dst, src);
        if (size == 15) return _fast_memcpy<15>(dst, src);
    }
    static const void* addrs[] = {
        && B0,
        && B1,
        && B2,
        && B3,
        && B4,
        && B5,
        && B6,
        && B7,
        && B8,
        && B9,
        && B10,
        && B11,
        && B12,
        && B13,
        && B14,
        && B15,
        && B16,
        && B17,
        && B18,
        && B19,
        && B20,
        && B21,
        && B22,
        && B23,
        && B24,
        && B25,
        && B26,
        && B27,
        && B28,
        && B29,
        && B30,
        && B31,
        && B32,
        && B33,
        && B34,
        && B35,
        && B36,
        && B37,
        && B38,
        && B39,
        && B40,
        && B41,
        && B42,
        && B43,
        && B44,
        && B45,
        && B46,
        && B47,
        && B48,
        && B49,
        && B50,
        && B51,
        && B52,
        && B53,
        && B54,
        && B55,
        && B56,
        && B57,
        && B58,
        && B59,
        && B60,
        && B61,
        && B62,
        && B63,
        && B64,
        && B65,
        && B66,
        && B67,
        && B68,
        && B69,
        && B70,
        && B71,
        && B72,
        && B73,
        && B74,
        && B75,
        && B76,
        && B77,
        && B78,
        && B79,
        && B80,
        && B81,
        && B82,
        && B83,
        && B84,
        && B85,
        && B86,
        && B87,
        && B88,
        && B89,
        && B90,
        && B91,
        && B92,
        && B93,
        && B94,
        && B95,
        && B96,
        && B97,
        && B98,
        && B99,
        && B100,
        && B101,
        && B102,
        && B103,
        && B104,
        && B105,
        && B106,
        && B107,
        && B108,
        && B109,
        && B110,
        && B111,
        && B112,
        && B113,
        && B114,
        && B115,
        && B116,
        && B117,
        && B118,
        && B119,
        && B120,
        && B121,
        && B122,
        && B123,
        && B124,
        && B125,
        && B126,
        && B127,
        && B128,
        && B129,
        && B130,
        && B131,
        && B132,
        && B133,
        && B134,
        && B135,
        && B136,
        && B137,
        && B138,
        && B139,
        && B140,
        && B141,
        && B142,
        && B143,
        && B144,
        && B145,
        && B146,
        && B147,
        && B148,
        && B149,
        && B150,
        && B151,
        && B152,
        && B153,
        && B154,
        && B155,
        && B156,
        && B157,
        && B158,
        && B159,
        && B160,
        && B161,
        && B162,
        && B163,
        && B164,
        && B165,
        && B166,
        && B167,
        && B168,
        && B169,
        && B170,
        && B171,
        && B172,
        && B173,
        && B174,
        && B175,
        && B176,
        && B177,
        && B178,
        && B179,
        && B180,
        && B181,
        && B182,
        && B183,
        && B184,
        && B185,
        && B186,
        && B187,
        && B188,
        && B189,
        && B190,
        && B191,
        && B192,
        && B193,
        && B194,
        && B195,
        && B196,
        && B197,
        && B198,
        && B199,
        && B200,
        && B201,
        && B202,
        && B203,
        && B204,
        && B205,
        && B206,
        && B207,
        && B208,
        && B209,
        && B210,
        && B211,
        && B212,
        && B213,
        && B214,
        && B215,
        && B216,
        && B217,
        && B218,
        && B219,
        && B220,
        && B221,
        && B222,
        && B223,
        && B224,
        && B225,
        && B226,
        && B227,
        && B228,
        && B229,
        && B230,
        && B231,
        && B232,
        && B233,
        && B234,
        && B235,
        && B236,
        && B237,
        && B238,
        && B239,
        && B240,
        && B241,
        && B242,
        && B243,
        && B244,
        && B245,
        && B246,
        && B247,
        && B248,
        && B249,
        && B250,
        && B251,
        && B252,
        && B253,
        && B254,
        && B255
    };
    if(size <= 255) {
        goto* addrs[size];
    B0:
    B1:
    B2:
    B3:
    B4:
    B5:
    B6:
    B7:
    B8:
    B9:
    B10:
    B11:
    B12:
    B13:
    B14:
    B15:
    B16:
        return _fast_memcpy<16>(dst, src);
    B17:
        return _fast_memcpy<17>(dst, src);
    B18:
        return _fast_memcpy<18>(dst, src);
    B19:
        return _fast_memcpy<19>(dst, src);
    B20:
        return _fast_memcpy<20>(dst, src);
    B21:
        return _fast_memcpy<21>(dst, src);
    B22:
        return _fast_memcpy<22>(dst, src);
    B23:
        return _fast_memcpy<23>(dst, src);
    B24:
        return _fast_memcpy<24>(dst, src);
    B25:
        return _fast_memcpy<25>(dst, src);
    B26:
        return _fast_memcpy<26>(dst, src);
    B27:
        return _fast_memcpy<27>(dst, src);
    B28:
        return _fast_memcpy<28>(dst, src);
    B29:
        return _fast_memcpy<29>(dst, src);
    B30:
        return _fast_memcpy<30>(dst, src);
    B31:
        return _fast_memcpy<31>(dst, src);
    B32:
        return _fast_memcpy<32>(dst, src);
    B33:
        return _fast_memcpy<33>(dst, src);
    B34:
        return _fast_memcpy<34>(dst, src);
    B35:
        return _fast_memcpy<35>(dst, src);
    B36:
        return _fast_memcpy<36>(dst, src);
    B37:
        return _fast_memcpy<37>(dst, src);
    B38:
        return _fast_memcpy<38>(dst, src);
    B39:
        return _fast_memcpy<39>(dst, src);
    B40:
        return _fast_memcpy<40>(dst, src);
    B41:
        return _fast_memcpy<41>(dst, src);
    B42:
        return _fast_memcpy<42>(dst, src);
    B43:
        return _fast_memcpy<43>(dst, src);
    B44:
        return _fast_memcpy<44>(dst, src);
    B45:
        return _fast_memcpy<45>(dst, src);
    B46:
        return _fast_memcpy<46>(dst, src);
    B47:
        return _fast_memcpy<47>(dst, src);
    B48:
        return _fast_memcpy<48>(dst, src);
    B49:
        return _fast_memcpy<49>(dst, src);
    B50:
        return _fast_memcpy<50>(dst, src);
    B51:
        return _fast_memcpy<51>(dst, src);
    B52:
        return _fast_memcpy<52>(dst, src);
    B53:
        return _fast_memcpy<53>(dst, src);
    B54:
        return _fast_memcpy<54>(dst, src);
    B55:
        return _fast_memcpy<55>(dst, src);
    B56:
        return _fast_memcpy<56>(dst, src);
    B57:
        return _fast_memcpy<57>(dst, src);
    B58:
        return _fast_memcpy<58>(dst, src);
    B59:
        return _fast_memcpy<59>(dst, src);
    B60:
        return _fast_memcpy<60>(dst, src);
    B61:
        return _fast_memcpy<61>(dst, src);
    B62:
        return _fast_memcpy<62>(dst, src);
    B63:
        return _fast_memcpy<63>(dst, src);
    B64:
        return _fast_memcpy<64>(dst, src);
    B65:
        return _fast_memcpy<65>(dst, src);
    B66:
        return _fast_memcpy<66>(dst, src);
    B67:
        return _fast_memcpy<67>(dst, src);
    B68:
        return _fast_memcpy<68>(dst, src);
    B69:
        return _fast_memcpy<69>(dst, src);
    B70:
        return _fast_memcpy<70>(dst, src);
    B71:
        return _fast_memcpy<71>(dst, src);
    B72:
        return _fast_memcpy<72>(dst, src);
    B73:
        return _fast_memcpy<73>(dst, src);
    B74:
        return _fast_memcpy<74>(dst, src);
    B75:
        return _fast_memcpy<75>(dst, src);
    B76:
        return _fast_memcpy<76>(dst, src);
    B77:
        return _fast_memcpy<77>(dst, src);
    B78:
        return _fast_memcpy<78>(dst, src);
    B79:
        return _fast_memcpy<79>(dst, src);
    B80:
        return _fast_memcpy<80>(dst, src);
    B81:
        return _fast_memcpy<81>(dst, src);
    B82:
        return _fast_memcpy<82>(dst, src);
    B83:
        return _fast_memcpy<83>(dst, src);
    B84:
        return _fast_memcpy<84>(dst, src);
    B85:
        return _fast_memcpy<85>(dst, src);
    B86:
        return _fast_memcpy<86>(dst, src);
    B87:
        return _fast_memcpy<87>(dst, src);
    B88:
        return _fast_memcpy<88>(dst, src);
    B89:
        return _fast_memcpy<89>(dst, src);
    B90:
        return _fast_memcpy<90>(dst, src);
    B91:
        return _fast_memcpy<91>(dst, src);
    B92:
        return _fast_memcpy<92>(dst, src);
    B93:
        return _fast_memcpy<93>(dst, src);
    B94:
        return _fast_memcpy<94>(dst, src);
    B95:
        return _fast_memcpy<95>(dst, src);
    B96:
        return _fast_memcpy<96>(dst, src);
    B97:
        return _fast_memcpy<97>(dst, src);
    B98:
        return _fast_memcpy<98>(dst, src);
    B99:
        return _fast_memcpy<99>(dst, src);
    B100:
        return _fast_memcpy<100>(dst, src);
    B101:
        return _fast_memcpy<101>(dst, src);
    B102:
        return _fast_memcpy<102>(dst, src);
    B103:
        return _fast_memcpy<103>(dst, src);
    B104:
        return _fast_memcpy<104>(dst, src);
    B105:
        return _fast_memcpy<105>(dst, src);
    B106:
        return _fast_memcpy<106>(dst, src);
    B107:
        return _fast_memcpy<107>(dst, src);
    B108:
        return _fast_memcpy<108>(dst, src);
    B109:
        return _fast_memcpy<109>(dst, src);
    B110:
        return _fast_memcpy<110>(dst, src);
    B111:
        return _fast_memcpy<111>(dst, src);
    B112:
        return _fast_memcpy<112>(dst, src);
    B113:
        return _fast_memcpy<113>(dst, src);
    B114:
        return _fast_memcpy<114>(dst, src);
    B115:
        return _fast_memcpy<115>(dst, src);
    B116:
        return _fast_memcpy<116>(dst, src);
    B117:
        return _fast_memcpy<117>(dst, src);
    B118:
        return _fast_memcpy<118>(dst, src);
    B119:
        return _fast_memcpy<119>(dst, src);
    B120:
        return _fast_memcpy<120>(dst, src);
    B121:
        return _fast_memcpy<121>(dst, src);
    B122:
        return _fast_memcpy<122>(dst, src);
    B123:
        return _fast_memcpy<123>(dst, src);
    B124:
        return _fast_memcpy<124>(dst, src);
    B125:
        return _fast_memcpy<125>(dst, src);
    B126:
        return _fast_memcpy<126>(dst, src);
    B127:
        return _fast_memcpy<127>(dst, src);
    B128:
        return _fast_memcpy<128>(dst, src);
    B129:
        return _fast_memcpy<129>(dst, src);
    B130:
        return _fast_memcpy<130>(dst, src);
    B131:
        return _fast_memcpy<131>(dst, src);
    B132:
        return _fast_memcpy<132>(dst, src);
    B133:
        return _fast_memcpy<133>(dst, src);
    B134:
        return _fast_memcpy<134>(dst, src);
    B135:
        return _fast_memcpy<135>(dst, src);
    B136:
        return _fast_memcpy<136>(dst, src);
    B137:
        return _fast_memcpy<137>(dst, src);
    B138:
        return _fast_memcpy<138>(dst, src);
    B139:
        return _fast_memcpy<139>(dst, src);
    B140:
        return _fast_memcpy<140>(dst, src);
    B141:
        return _fast_memcpy<141>(dst, src);
    B142:
        return _fast_memcpy<142>(dst, src);
    B143:
        return _fast_memcpy<143>(dst, src);
    B144:
        return _fast_memcpy<144>(dst, src);
    B145:
        return _fast_memcpy<145>(dst, src);
    B146:
        return _fast_memcpy<146>(dst, src);
    B147:
        return _fast_memcpy<147>(dst, src);
    B148:
        return _fast_memcpy<148>(dst, src);
    B149:
        return _fast_memcpy<149>(dst, src);
    B150:
        return _fast_memcpy<150>(dst, src);
    B151:
        return _fast_memcpy<151>(dst, src);
    B152:
        return _fast_memcpy<152>(dst, src);
    B153:
        return _fast_memcpy<153>(dst, src);
    B154:
        return _fast_memcpy<154>(dst, src);
    B155:
        return _fast_memcpy<155>(dst, src);
    B156:
        return _fast_memcpy<156>(dst, src);
    B157:
        return _fast_memcpy<157>(dst, src);
    B158:
        return _fast_memcpy<158>(dst, src);
    B159:
        return _fast_memcpy<159>(dst, src);
    B160:
        return _fast_memcpy<160>(dst, src);
    B161:
        return _fast_memcpy<161>(dst, src);
    B162:
        return _fast_memcpy<162>(dst, src);
    B163:
        return _fast_memcpy<163>(dst, src);
    B164:
        return _fast_memcpy<164>(dst, src);
    B165:
        return _fast_memcpy<165>(dst, src);
    B166:
        return _fast_memcpy<166>(dst, src);
    B167:
        return _fast_memcpy<167>(dst, src);
    B168:
        return _fast_memcpy<168>(dst, src);
    B169:
        return _fast_memcpy<169>(dst, src);
    B170:
        return _fast_memcpy<170>(dst, src);
    B171:
        return _fast_memcpy<171>(dst, src);
    B172:
        return _fast_memcpy<172>(dst, src);
    B173:
        return _fast_memcpy<173>(dst, src);
    B174:
        return _fast_memcpy<174>(dst, src);
    B175:
        return _fast_memcpy<175>(dst, src);
    B176:
        return _fast_memcpy<176>(dst, src);
    B177:
        return _fast_memcpy<177>(dst, src);
    B178:
        return _fast_memcpy<178>(dst, src);
    B179:
        return _fast_memcpy<179>(dst, src);
    B180:
        return _fast_memcpy<180>(dst, src);
    B181:
        return _fast_memcpy<181>(dst, src);
    B182:
        return _fast_memcpy<182>(dst, src);
    B183:
        return _fast_memcpy<183>(dst, src);
    B184:
        return _fast_memcpy<184>(dst, src);
    B185:
        return _fast_memcpy<185>(dst, src);
    B186:
        return _fast_memcpy<186>(dst, src);
    B187:
        return _fast_memcpy<187>(dst, src);
    B188:
        return _fast_memcpy<188>(dst, src);
    B189:
        return _fast_memcpy<189>(dst, src);
    B190:
        return _fast_memcpy<190>(dst, src);
    B191:
        return _fast_memcpy<191>(dst, src);
    B192:
        return _fast_memcpy<192>(dst, src);
    B193:
        return _fast_memcpy<193>(dst, src);
    B194:
        return _fast_memcpy<194>(dst, src);
    B195:
        return _fast_memcpy<195>(dst, src);
    B196:
        return _fast_memcpy<196>(dst, src);
    B197:
        return _fast_memcpy<197>(dst, src);
    B198:
        return _fast_memcpy<198>(dst, src);
    B199:
        return _fast_memcpy<199>(dst, src);
    B200:
        return _fast_memcpy<200>(dst, src);
    B201:
        return _fast_memcpy<201>(dst, src);
    B202:
        return _fast_memcpy<202>(dst, src);
    B203:
        return _fast_memcpy<203>(dst, src);
    B204:
        return _fast_memcpy<204>(dst, src);
    B205:
        return _fast_memcpy<205>(dst, src);
    B206:
        return _fast_memcpy<206>(dst, src);
    B207:
        return _fast_memcpy<207>(dst, src);
    B208:
        return _fast_memcpy<208>(dst, src);
    B209:
        return _fast_memcpy<209>(dst, src);
    B210:
        return _fast_memcpy<210>(dst, src);
    B211:
        return _fast_memcpy<211>(dst, src);
    B212:
        return _fast_memcpy<212>(dst, src);
    B213:
        return _fast_memcpy<213>(dst, src);
    B214:
        return _fast_memcpy<214>(dst, src);
    B215:
        return _fast_memcpy<215>(dst, src);
    B216:
        return _fast_memcpy<216>(dst, src);
    B217:
        return _fast_memcpy<217>(dst, src);
    B218:
        return _fast_memcpy<218>(dst, src);
    B219:
        return _fast_memcpy<219>(dst, src);
    B220:
        return _fast_memcpy<220>(dst, src);
    B221:
        return _fast_memcpy<221>(dst, src);
    B222:
        return _fast_memcpy<222>(dst, src);
    B223:
        return _fast_memcpy<223>(dst, src);
    B224:
        return _fast_memcpy<224>(dst, src);
    B225:
        return _fast_memcpy<225>(dst, src);
    B226:
        return _fast_memcpy<226>(dst, src);
    B227:
        return _fast_memcpy<227>(dst, src);
    B228:
        return _fast_memcpy<228>(dst, src);
    B229:
        return _fast_memcpy<229>(dst, src);
    B230:
        return _fast_memcpy<230>(dst, src);
    B231:
        return _fast_memcpy<231>(dst, src);
    B232:
        return _fast_memcpy<232>(dst, src);
    B233:
        return _fast_memcpy<233>(dst, src);
    B234:
        return _fast_memcpy<234>(dst, src);
    B235:
        return _fast_memcpy<235>(dst, src);
    B236:
        return _fast_memcpy<236>(dst, src);
    B237:
        return _fast_memcpy<237>(dst, src);
    B238:
        return _fast_memcpy<238>(dst, src);
    B239:
        return _fast_memcpy<239>(dst, src);
    B240:
        return _fast_memcpy<240>(dst, src);
    B241:
        return _fast_memcpy<241>(dst, src);
    B242:
        return _fast_memcpy<242>(dst, src);
    B243:
        return _fast_memcpy<243>(dst, src);
    B244:
        return _fast_memcpy<244>(dst, src);
    B245:
        return _fast_memcpy<245>(dst, src);
    B246:
        return _fast_memcpy<246>(dst, src);
    B247:
        return _fast_memcpy<247>(dst, src);
    B248:
        return _fast_memcpy<248>(dst, src);
    B249:
        return _fast_memcpy<249>(dst, src);
    B250:
        return _fast_memcpy<250>(dst, src);
    B251:
        return _fast_memcpy<251>(dst, src);
    B252:
        return _fast_memcpy<252>(dst, src);
    B253:
        return _fast_memcpy<253>(dst, src);
    B254:
        return _fast_memcpy<254>(dst, src);
    B255:
        return _fast_memcpy<255>(dst, src);
    }
    ::memcpy(dst, src, size);
    return ;
}

} // namespace share

#endif // __CC_SHARE_FAST_MEMCPY_H__
