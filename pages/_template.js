import Head from 'next/head';

class Page extends React.Component {
  render() {
    return (
        <div>
        <Head>
        <title>Ayobi</title>
        <meta http-equiv="x-ua-compatible" content="ie=edge"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway:400,800"/>
        <link rel='stylesheet' href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"/>
        <link rel='stylesheet' href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"/>
        <link rel='stylesheet' href="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js"/>
        <link rel="stylesheet" href="/static/styles.css"/>
        <link href="//cdn-images.mailchimp.com/embedcode/classic-10_7.css" rel="stylesheet" type="text/css"/>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"/>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"/>
        </Head>
        <div style={{fontFamily: 'Noto Sans, sans-serif', margin: 0, padding: 0}}>
        {this.props.children}
        </div>
        </div>
        )
  }
}

export default Page;
