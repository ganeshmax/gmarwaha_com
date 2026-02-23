/**
 * Lavalamp for jQuery Lovers - Modern Recreation
 * Original by Ganesh Marwaha (based on Mootools version by Guillermo Rauch)
 * Recreated for modern jQuery compatibility without image sprite dependencies.
 */
(function ($) {
    $.fn.lavaLamp = function (o) {
        o = $.extend({
            fx: "swing",
            speed: 500,
            click: function () { }
        }, o || {});

        return this.each(function () {
            var b = $(this),
                noop = function () { },
                $back = $('<li class="back"><div class="left"></div></li>').appendTo(b),
                $li = $("li:not(.back)", this),
                curr = $("li.current", this)[0] || $($li[0]).addClass("current")[0];

            $li.each(function () {
                var me = this;
                $(me).hover(function () {
                    move(me);
                }, noop);
            });

            $(this).hover(noop, function () {
                move(curr);
            });

            $li.click(function (e) {
                setCurr(this);
                return o.click.apply(this, [e, this]);
            });

            setCurr(curr);

            // Immediate jump to initial position without animation on load
            $back.css({
                "left": curr.offsetLeft + "px",
                "width": curr.offsetWidth + "px"
            });

            function setCurr(el) {
                $back.css({
                    "left": el.offsetLeft + "px",
                    "width": el.offsetWidth + "px"
                });
                curr = el;
            }

            function move(el) {
                $back.each(function () {
                    $(this).dequeue();
                }).animate({
                    width: el.offsetWidth,
                    left: el.offsetLeft
                }, o.speed, o.fx);
            }
        });
    };
})(jQuery);
