/**
 * jQuery.fn.equelizeHeights(uniform)
 * If `uniform` is `true`, all elements will have the same height.
 * Otherwise, the equalization will be on a line-basis.
 *
 * Copyright (C) 2013 Henrique Barcelos 
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.

 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>
 */
(function($){
    $.fn.equalizeHeights = function(uniform){
        var elems = $(this);

        var lineBasisEqualization = function() {
            var maxHeight = undefined;
            var lineObjects = [];
            var offsetTopFirst = elems.eq(0).offset().top;
            elems.each(function(i){
                if(offsetTopFirst != $(this).offset().top) {
                    $(lineObjects).height(maxHeight);
                    lineObjects = [this];
                    offsetTopFirst = $(this).offset().top;
                    maxHeight = undefined;
                } else {
                    if($(this).height() > maxHeight) {
                        maxHeight=$(this).height();
                    }
                    lineObjects.push(this);
                }
                // For the last row an just if there are more than one element in the row
                if(i == elems.size() - 1 && maxHeight !== undefined) {
                    $(lineObjects).height(maxHeight);
                }
            });
        }

        var uniformEqualization = function() {
            var maxHeight = 0;
            elems.each(function(i){
                if($(this).height() > maxHeight) {
                    maxHeight=$(this).height();
                }
            });
            elems.height(maxHeight);
        }

        if(uniform === true) {
            uniformEqualization();
        } else {
            lineBasisEqualization();
        }
        return this;
    };
})(jQuery);
