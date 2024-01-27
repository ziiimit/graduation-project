const anime = require('anime-master/lib/anime.min.js')

function StackFx(el) {
    this.DOM = {};
    this.DOM.el = el;
    this.DOM.stack = this.DOM.el.querySelector('.stack');
    this.DOM.stackItems = [].slice.call(this.DOM.stack.children);
    this.totalItems = this.DOM.stackItems.length;
}

StackFx.prototype._removeAnimeTargets = function () {
    anime.remove(this.DOM.stackItems);
};

function AltairFx(el) {
    StackFx.call(this, el);
    this._initEvents();
}

AltairFx.prototype = Object.create(StackFx.prototype);
AltairFx.prototype.constructor = AltairFx;

AltairFx.prototype._initEvents = function () {
    var self = this;
    this._mouseenterFn = function () {
        self._removeAnimeTargets();
        self._in();
    };
    this._mouseleaveFn = function () {
        self._removeAnimeTargets();
        self._out();
    };
    this.DOM.stack.addEventListener('mouseenter', this._mouseenterFn);
    this.DOM.stack.addEventListener('mouseleave', this._mouseleaveFn);
};

AltairFx.prototype._in = function () {
    var self = this;

    this.DOM.stackItems.map(function (e, i) {
        e.style.opacity = i !== self.totalItems - 1 ? 0.2 * i + 0.2 : 1
    });

    anime({
        targets: this.DOM.stackItems,
        duration: 1000,
        easing: 'easeOutElastic',
        translateZ: function (target, index, cnt) {
            return index * 3;
        },
        rotateX: function (target, index, cnt) {
            return -1 * index * 4;
        },
        delay: function (target, index, cnt) {
            return (cnt - index - 1) * 30
        }
    });
};

AltairFx.prototype._out = function () {
    var self = this;

    anime({
        targets: this.DOM.stackItems,
        duration: 500,
        easing: 'easeOutExpo',
        opacity: function (target, index, cnt) {
            return index !== cnt - 1 ? 0 : 1
        },
        translateZ: 0,
        rotateX: 0
    });
};




module.exports = {
    AltairFx: AltairFx
}