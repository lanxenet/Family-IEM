function valid(txt) {
	var i = 0;
	var len = txt.length;
	for (i = 0; i < len; i++) {
		var checkTxt = txt.charCodeAt(i); // 使用charCodeAt方法，方法可返回指定位置的字符的
		// Unicode 编码。这个返回值是 0 - 65535
		// 之间的整数。
		if (checkTxt == 37 || checkTxt == 8 || checkTxt == 39 || checkTxt == 46
				|| checkTxt == 190 || checkTxt == 110
				|| (checkTxt >= 48 && checkTxt <= 57)
				|| (checkTxt >= 96 && checkTxt <= 105)) {
			continue;
		} else {
			return false;
		}
	}
	return true;

}

function onkeydownEvent() {
	if (event.keyCode == 37 || event.keyCode == 8 || event.keyCode == 9
			|| event.keyCode == 39 || event.keyCode == 46
			|| event.keyCode == 190 || event.keyCode == 110
			|| (event.keyCode >= 48 && event.keyCode <= 57)
			|| (event.keyCode >= 96 && event.keyCode <= 105)) {
	} else {
		return false;
	}
}

function onblurEvent() {
	this.value = format(this.value);
}

function format(money) {
	if (/[^0-9\.]/.test(money))
		return money;
	money = money.replace(/^(\d*)$/, "$1.");
	money = (money + "00").replace(/(\d*\.\d\d)\d*/, "$1");
	money = money.replace(".", ",");
	var re = /(\d)(\d{3},)/;
	while (re.test(money)) {
		money = money.replace(re, "$1,$2");
	}
	money = money.replace(/,(\d\d)$/, ".$1");
	return money.replace(/^\./, "0.")
}

Date.prototype.format = function(fmt) {
	var o = {
		"M+" : this.getMonth() + 1,
		// 月份
		"d+" : this.getDate(),
		// 日
		"h+" : this.getHours() % 12 == 0 ? 12 : this.getHours() % 12,
		// 小时
		"H+" : this.getHours(),
		// 小时
		"m+" : this.getMinutes(),
		// 分
		"s+" : this.getSeconds(),
		// 秒
		"q+" : Math.floor((this.getMonth() + 3) / 3),
		// 季度
		"S" : this.getMilliseconds()
	// 毫秒
	};
	var week = {
		"0" : "\u65e5",
		"1" : "\u4e00",
		"2" : "\u4e8c",
		"3" : "\u4e09",
		"4" : "\u56db",
		"5" : "\u4e94",
		"6" : "\u516d"
	};
	if (/(y+)/.test(fmt)) {
		fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "")
				.substr(4 - RegExp.$1.length));
	}
	if (/(E+)/.test(fmt)) {
		fmt = fmt
				.replace(
						RegExp.$1,
						((RegExp.$1.length > 1) ? (RegExp.$1.length > 2 ? "\u661f\u671f"
								: "\u5468")
								: "")
								+ week[this.getDay() + ""]);
	}
	for ( var k in o) {
		if (new RegExp("(" + k + ")").test(fmt)) {
			fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k])
					: (("00" + o[k]).substr(("" + o[k]).length)));
		}
	}
	return fmt;
}