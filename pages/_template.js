import Head from 'next/head';

class Page extends React.Component {
  render() {
    return (
        <div>
        <Head>
        <link href="https://fonts.googleapis.com/css?family=Noto+Sans" rel="stylesheet"/>
        </Head>
        <div style={{fontFamily: 'Noto Sans, sans-serif', margin: 0, padding: 0}}>
        {this.props.children}
        </div>
        </div>
        )
  }
}

export default Page;
