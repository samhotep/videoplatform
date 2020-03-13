import React from 'react';
import TitleBar from '../components/headers/titleBar';

function ContainerRow(){
    return (
        <div style={styles.container}>
        </div>
    )
}

const styles = {
    
    container: {
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center'
    }

}

export default ContainerRow;
