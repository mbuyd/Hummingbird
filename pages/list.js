import Layout from '../components/Layout';
import listReactFiles from 'list-react-files'

export default function About() {
    listReactFiles(__dirname).then(files => console.log(files))
    
    return (
        <Layout>
            <p>This is the about page</p>
        </Layout>
    );
}