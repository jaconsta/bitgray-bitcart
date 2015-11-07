/**********************************/
/* reactView.js
/*
/*
/**********************************/

var UserSearch = React.createClass({
  render:function () {
    return (
      <div className="row">
        <div className="col-xs-12 col-md-8">
            <h2>Find billing from user Id card.</h2>
            <form className="form-inline">
                <div className="form-group">
                    <label>User Id:</label>
                    <input type="text" className="form-control" id="userId" placeholder="User Identification" />
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
      totalPrice += product.price;
      return (
        <ProductDetails id={product.id} product={product.product} office={product.office} price={product.price} />
        );
    });
    return (
      <div className="row">
        <div className="col-xs-12 col-md-8"> <h2>Search results.</h2></div>
        <UserDetails idCard={this.props.userDetails[0].idCard} name={this.props.userDetails[0].name}></UserDetails>
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
  render: function () {
    return (
      <div className="UserReport">
        <h1>Billing viewer</h1>
        <UserSearch />
        <UserResults data={this.props.data} userDetails={userDetails}/>
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
  <UserReport data={userProducts} userDetails={userDetails}/>,
  document.getElementById('content')
);