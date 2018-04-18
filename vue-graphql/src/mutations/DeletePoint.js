import gql from 'graphql-tag'

export default gql`
  mutation deletePoint($id: ID!) {
    deletePoint(input: {id: $id}) 
    {
        id
      }
  }
`
