(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{193:function(e,t,n){e.exports=n(378)},378:function(e,t,n){"use strict";n.r(t);var a=n(1),r=n.n(a),s=n(17),c=n.n(s),o=n(94),i=n(50),l=n.n(i),u=n(91),p=n(146),d=n(147),h=n(161),m=n(160),f=n(41),k=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};return y(e,t)},y=function(e,t){var n=localStorage.getItem("token"),a="http://127.0.0.1:8000/api/"+e,r=t.method||"GET";return t.headers=t.headers||{},t.headers.Accept="application/json",t.headers["Content-Type"]="application/json",void 0!==n&&(t.headers.Authorization=n),new Promise((function(e,n){var s=new XMLHttpRequest;s.open(r,a),s.onload=function(){if(this.status>=200&&this.status<300)e(JSON.parse(s.response));else{var t=JSON.parse(s.response).error;n({status:t.status,statusText:t.message})}},s.onerror=function(){var e=JSON.parse(s.response).error;n({status:e.status,statusText:e.message})},t.headers&&Object.keys(t.headers).forEach((function(e){s.setRequestHeader(e,t.headers[e])}));var c=t.params;c&&"object"===typeof c&&(c=Object.keys(c).map((function(e){return encodeURIComponent(e)+"="+encodeURIComponent(c[e])})).join("&")),s.send(c)}))},b=n(395),v=n(396),E=n(400),g=n(397),O=n(398),j=n(401),S=function(e){Object(h.a)(n,e);var t=Object(m.a)(n);function n(e){var a;return Object(p.a)(this,n),(a=t.call(this,e)).componentDidMount=Object(u.a)(l.a.mark((function e(){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:k("stocks/").then((function(e){a.setState({ticker_list:e})}));case 1:case"end":return e.stop()}}),e)}))),a.getPriceHistory=function(){var e=Object(u.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:k("pricehistorys/?symbol="+t).then((function(e){var n=a.state.prices;n[t]=e,a.setState({prices:n})}));case 1:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),a.state={ticker_list:[],selected_tickers:[],prices:{}},a}return Object(d.a)(n,[{key:"handleSelection",value:function(e){console.log(e);var t=Object(o.a)(this.state.selected_tickers);console.log(t);var n=t.indexOf(e);-1===n?(this.setState({selected_tickers:[].concat(Object(o.a)(t),[e])}),this.getPriceHistory(e)):this.setState({selected_tickers:t.splice(n,1)})}},{key:"renderLineChart",value:function(){var e=Object.keys(this.state.prices);if(console.log(e.length),console.log(this.state.prices[e[0]]),0!==e.length)return r.a.createElement(b.a,null,r.a.createElement(f.c,{width:600,height:300,data:this.state.prices[e[0]]},r.a.createElement(f.b,{type:"monotone",dataKey:"close",stroke:"#8884d8"}),r.a.createElement(f.a,{stroke:"#ccc"}),r.a.createElement(f.d,{dataKey:"price_date"}),r.a.createElement(f.e,null)))}},{key:"render",value:function(){var e=this;return r.a.createElement(b.a,null,"Hello",r.a.createElement(v.a,null,this.state.ticker_list.map((function(t){return r.a.createElement(E.a,{key:t.symbol,role:void 0,dense:!0,button:!0,onClick:function(){e.handleSelection(t.symbol)}},r.a.createElement(g.a,null,r.a.createElement(O.a,{edge:"start",checked:-1!==e.state.selected_tickers.indexOf(t.symbol),disableRipple:!0})),r.a.createElement(j.a,{id:t.symbol,primary:t.symbol}))}))),this.renderLineChart())}}]),n}(r.a.Component);c.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(S,null)),document.getElementById("root"))}},[[193,1,2]]]);
//# sourceMappingURL=main.9671a218.chunk.js.map