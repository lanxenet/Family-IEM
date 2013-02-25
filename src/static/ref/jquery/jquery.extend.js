/*!
 * Name: jquery.extend.js
 **/
(function($){
	if (typeof(console)=='undefined') {
		console = {
			log: function() {
			}
		}
	}
	var imageCache = [];
	$.fn.firstParent = function(selector) {
		return this.parents(selector).first();
	};
	$.fn.detectFocus = function() {
		this.focus(function(){
			$(this).addClass("hasFocus");
		});
		this.blur(function(){
			$(this).removeClass("hasFocus");
		});
	};
	$.fn.liveDetectFocus = function() {
		this.live('focus',function(){
			$(this).addClass("hasFocus");
		});
		this.live('blur',function(){
			$(this).removeClass("hasFocus");
		});
	};
	$.fn.ajaxify = function(callback) {
		function applyCallback(self) {
			return function(response) {
				self.removeClass('loading');
				if (typeof(callback)=='function') {
					callback(response, self);
				}
			}
		}
		function doAjax(url, self, method) {
			var data = self.serialize();
			url += ((url.indexOf('?') == -1) ? '?' : '&') + 'ajax=1';
			if (method == 'post') {
				$.post(url, data, applyCallback(self), 'text');
			} else  {
				$.get(url, data, applyCallback(self), 'text');
			}
			return false;
		}
		function doClick(event) {
			var eventType = event.type.toLowerCase();
			var self = $(this);
			if (self.hasClass('disabled')) {
				return false;
			}
			var confirmText = self.data('confirm');
			if (confirmText && !confirm(confirmText)) {
				return false;
			}
			var href = self.attr('href');
			if (href && eventType == 'click') {
				self.addClass('loading');
				doAjax(href, self, 'get');
				//event.preventDefault();
				return false;
			}
			var action = self.attr('action');
			if (action && eventType == 'submit') {
				if (event.type=='submit') {
					self.addClass('loading');
					doAjax(action, self, 'post');
					//event.preventDefault();
					return false;
				}
			}
		}
		this.bind('click submit', doClick);
		this.addClass('ajaxified');
	};
	$.fn.born = function() {
		// TODO
	};
	$.fn.oddEven = function() {
		// jQuery count from 0, but PlayFramework count from 1
		this.removeClass('odd');
		this.removeClass('even');
		this.filter(':odd').addClass('even');
		this.filter(':even').addClass('odd');
	}

	$.fn.toggleSlide = function() {
		//TODO
	}

	// parseJH / getJH / postJH
	// JSON + "\n\n" + HTML
	$.extend({
		preloadImage: function(src) {
			var image = document.createElement('img');
			image.src = src;
			imageCache.push(image);
		},
		wbr: function(str) {
			var fragAry = [];
			for (var i=0;i<str.length;i=i+3) {
				var frag = str.substr(i,3);
				var fragLen=3;
				// prevent breaking html code
				while((frag.match(/<[^>]+$/))&&(fragLen<str.length-i)){
					fragLen++;
					frag = str.substr(i,fragLen);
				}
				// prevent breaking &...;
				while(
					(frag.match(/\&[a-zA-Z]{0,5}$/))
					&&str.substr(i+fragLen).match(/^[a-zA-Z]{0,5}\;/)
				){
					fragLen++;
					frag = str.substr(i,fragLen);
				}
				i+=(fragLen-3);
				fragAry.push(frag);
			}
			var newStr = fragAry.join('<wbr/>');
			return newStr;
		},
		parseJH: function(response) {
			var json, html
			var index = response.indexOf("\n\n<!--JH-->\n");
			if (index == -1) {
				index = response.indexOf("\r\n\r\n<!--JH-->\r\n");
			}
			if (index != -1) {
				json = response.substr(0, index);
				html = response.substr(index + 2);
			} else {
				json = response;
			}
			json = $.parseJSON(json) || {"ret":-1,"status":-1}; //migrating 'ret'(stupid) to 'status'
			return {
				"json": json,
				"html": html
			};
		},

		getJH: function(url, data, callback) {
			if ( jQuery.isFunction( data ) ) {
				callback = data;
				data = null;
			}
			function processResponse(response) {
				callback($.parseJH(response));
			}
			return $.get(url, data, processResponse, 'text');
		},

		postJH: function(url, data, callback) {
			if ( jQuery.isFunction( data ) ) {
				callback = data;
				data = {};
			}
			function processResponse(response) {
				callback($.parseJH(response));
			}
			return $.post(url, data, callback, 'text');
		}
	});
})(jQuery);
