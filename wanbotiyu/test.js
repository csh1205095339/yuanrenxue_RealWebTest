var _i_cs = {
    _i_gg: false,
    _i_gh: new Array,
    _i_gi: new Array,
    _i_gj: 4e3,
    toString: function() {
        var e = 0;
        var i = "";
        for (var _ in this._i_gh) {
            if (this._i_gj <= 0 || typeof this._i_gh[_] == "string" && i.length + _.length + this._i_gh[_].length + 8 < this._i_gj * 3 / 4 - 4) {
                e++;
                i += _i_e_frmt.__if_r_DecToHex(_.length, 4) + _.toUpperCase() + _i_e_frmt.__if_r_DecToHex(this._i_gh[_].length, 4) + this._i_gh[_]
            }
        }
        return i
    },
    __if_da_DoQryStg: function() {
        try {
            var e = "";
            for (var i in this._i_gi) {
                if (this._i_gj <= 0 || typeof this._i_gi[i] == "string" && this._i_gi[i].length + e.length < this._i_gj + 1) {
                    if (e.length > 0)
                        e += ";";
                    e += this._i_gi[i]
                }
            }
            var _ = this.toString();
            var t = _;
            if (this._i_gj <= 0 || t.length + e.length < this._i_gj + 1)
                e = e.length > 0 ? t + ";" + e : t;
            return e
        } catch (r) {}
    },
    __if_ds: function(e) {
        return e && typeof e == "string" && e.length > 0
    },
    __if_ek: function(e) {
        if (typeof e != "string" || this._i_gj > 0 && e.length > this._i_gj)
            return;
        this._i_gi[this._i_gi.length] = e
    },
    __if_fd_SetArr: function(e, i) {
        if (this.__if_ds(e) && this.__if_ds(i))
            this._i_gh[e] = i
    },
    __if_fx: function(e) {
        if (typeof e != "string")
            return;
        var i = 4;
        var _ = 0;
        var t = new Array(2);
        do {
            var r = parseInt(e.substr(i, 4), 16);
            if (isNaN(r) || r < 0)
                break;
            i += 4;
            _++;
            if (r > 0) {
                t[(_ - 1) % 2] = e.substr(i, r);
                i += r
            }
            if (!(_ % 2)) {
                this.__if_fd_SetArr(t[0], t[1]);
                t[0] = t[1] = ""
            }
        } while (i < e.length);
        this.__if_gs(true)
    },
    __if_gs: function(e) {
        try {
            if (e || __if_j()) {
                checkCallBackExist(this.__if_da_DoQryStg(), __if_j());
                this._i_gg = true
            }
            return true
        } catch (i) {
            __if_b_setErrExp("e2_bb_callback", i);
            return false
        }
    }
};

function E2GetBlackbox() {
    return {
        blackbox: "0002" + encrypt(_i_cs.__if_da_DoQryStg()),
    }
}
function encrypt(e) {
    return _b_6._e_c(e)
}
var _b_6 = {
    _keyStr: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
    _e_c: function(e) {
        var i = "";
        var _, t, r, n, a, o, s;
        var f = 0;
        e = _b_6._u_en(e);
        while (f < e.length) {
            _ = e.charCodeAt(f++);
            t = e.charCodeAt(f++);
            r = e.charCodeAt(f++);
            n = _ >> 2;
            a = (_ & 3) << 4 | t >> 4;
            o = (t & 15) << 2 | r >> 6;
            s = r & 63;
            if (isNaN(t)) {
                o = s = 64
            } else if (isNaN(r)) {
                s = 64
            }
            i = i + this._keyStr.charAt(n) + this._keyStr.charAt(a) + this._keyStr.charAt(o) + this._keyStr.charAt(s)
        }
        return i
    },
    _u_en: function(e) {
        e = e.replace(/\r\n/g, "\n");
        var i = "";
        for (var _ = 0; _ < e.length; _++) {
            var t = e.charCodeAt(_);
            if (t < 128) {
                i += String.fromCharCode(t)
            } else if (t > 127 && t < 2048) {
                i += String.fromCharCode(t >> 6 | 192);
                i += String.fromCharCode(t & 63 | 128)
            } else {
                i += String.fromCharCode(t >> 12 | 224);
                i += String.fromCharCode(t >> 6 & 63 | 128);
                i += String.fromCharCode(t & 63 | 128)
            }
        }
        return i
    }
};

console.log(E2GetBlackbox())