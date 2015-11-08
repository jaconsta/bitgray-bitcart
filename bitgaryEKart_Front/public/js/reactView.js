/**********************************/
/* reactView.js
/*
/*
/**********************************/

var UserSearch = React.createClass({
  handleSubmit: function (e) {
    e.preventDefault(); // Avoid browser default action
    var userDocument = parseInt(this.refs.document.value.trim());
    // Validate fields
    if (!userDocument) {
      return;
    } else if (typeof(userDocument) != "number"){
      return;
    }
    // Send submit to server
    this.props.onCommentSubmit({userId: userDocument})
    // Clear form fields
    this.refs.document.value = '';
    return;
  },
  render:function () {
    return (
      <div className="row">
        <div className="col-xs-12 col-md-8">
            <h2>Find billing from user Id card.</h2>
            <form className="form-inline" onSubmit={this.handleSubmit}>
                <div className="form-group">
                    <label>User Id:</label>
                    <input type="text" className="form-control" id="userId" placeholder="User Identification" ref="document" />
                </div>
                <button type="submit" className="btn btn-primary">Find</button>
            </form>
        </div>
      </div>
    );
  }
});

var UserDetails = React.createClass({
  render: function() {
    return (
      <div className="userDetails">
        <div className="col-xs-6 col-md4"><b>Document:</b> {this.props.idCard} </div>
        <div className="col-xs-6 col-md4"><b>Name:</b> {this.props.name} </div>
      </div>
    );
  }
});
var ProductDetails = React.createClass({
  render: function() {
    return (
      <tr>
          <td>{this.props.id}</td>
          <td>{this.props.product}</td>
          <td>{this.props.office}</td>
          <td>{this.props.price}</td>
      </tr>
    );
  }
});
var UserResults = React.createClass({
  render: function () {
    var totalPrice = 0;
    var productDetailsNodes = this.props.data.map(function (product) {
      totalPrice += product.Precio;
      return (
        <ProductDetails id={product.id} product={product.Producto.producto} office={product.Oficina.sede} price={product.Precio} />
        );
    });
    return (
      <div className="row">
        <div className="col-xs-12 col-md-8"> <h2>Search results.</h2></div>
        <UserDetails idCard={this.props.data[0].Cliente.documento} name={this.props.data[0].Cliente.nombre}></UserDetails>
        <div className="col-xs-12 col-md-8">
            <table className="table table-striped table-hover">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Product</th>
                        <th>Office</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {productDetailsNodes}
                </tbody>
                <tfoot>
                    <tr className="success">
                        <td></td>
                        <td></td>
                        <td>TOTAL</td>
                        <td>{totalPrice}</td>
                    </tr>
                </tfoot>
            </table>
        </div>
      </div>
    );
  }
});

var UserReport = React.createClass({
  getInitialState: function () {
    return {showResults: false, data:[], userDetails:[]};
  },
  handleUserSubmit: function (userDocument) {
    $.ajax({
      url: this.props.url + '?userId=' + userDocument.userId,
      type: 'GET',
      crossDomain: true,
      success: function (data){
        if (!data || !data.orders || data.orders.length < 1){
          console.log("No exists");
          this.setState({showResults: false, data:[], userDetails:[]});
        } else {
          // The user is the first from all orders
          var user = data.orders[0].Cliente;
          this.setState({showResults: true, data: data.orders, userDetails: user});
        }
      }.bind(this),
      error: function(xhr, status, err){
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  render: function () {
    return (
      <div className="UserReport">
        <h1>Billing viewer</h1>
        <UserSearch onCommentSubmit={this.handleUserSubmit} />
        { this.state.showResults ? 
          <UserResults data={this.state.data} userDetails={userDetails}/> :
          null
        }
      </div>
    );
  }
});

//** Testing Date **/
var userDetails = [
  {id:1, idCard:1130614420, name:'Javier Constaín'}
]
var userProducts = [
  {id:1, user:1, product:'Cellphone', office:'Cali', price:500000},
  {id:2, user:1, product:'PC', office:'Bogota', price:1000000}
]

// Render the app
ReactDOM.render(
  <UserReport url="http://localhost:8000/orders/" />,//data={userProducts} userDetails={userDetails}/>,
  document.getElementById('content')
);