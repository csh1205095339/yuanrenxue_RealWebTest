var CryptoJs = require('crypto-js')
console.log(CryptoJs.enc['Utf8'])


var p = {};
p.a = CryptoJs;
T = function(e) {
            console.log('T:' + arguments[0], arguments[1]);
            var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : ""
              , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}
              , a = t.enc
              , r = void 0 === a ? "Utf8" : a
              , c = t.mode
              , i = void 0 === c ? "ECB" : c
              , o = t.padding
              , u = void 0 === o ? "Pkcs7" : o;
              var d = p.a.enc[r].parse(n)
              , l = {
                mode: p.a.mode[i],
                padding: p.a.pad[u]
            }, s = p.a.TripleDES.encrypt(e, d, l);
            return s.toString()
        }

F = function(e) {
            console.log('F:' + arguments[0]);
            var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {};
            if (e && "string" === typeof e) {
                var t = n.text || "0"
                  , a = n.length || 24;
                if (e.length < a)
                    for (var r = e.length; r < a; r++)
                        e += t;
                else
                    e = e.substring(0, a);
                return e
            }
        }

K = function() {
            console.log('K:' + arguments[0]);
            var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "";
            return e.replace(/\s+/g, "")
        };

function getpassword(account, password) {
    var password = '~haohao9527';
    var account = "1205095339@qq.com";
    return encodeURI(Object(T)(password, Object(F)(Object(K)(account))));
}