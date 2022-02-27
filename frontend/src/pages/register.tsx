import { ChakraProvider, Button,Input,Center,Box,Text,FormControl,FormLabel,HStack,Spacer,Flex, color, chakra } from '@chakra-ui/react';
import { Image } from '@chakra-ui/react';

export default function login(){
  return (
   <ChakraProvider>
     <Center>
       <Box bg="white" boxShadow={"xl"} p="20" overflow={"hidden"} mt={"10"}  borderRadius='8px' >
        <Box h= "600px" w="400px" mt={"-6"} mx={"-6"} pos="relative">
          <Center>
            <Image boxSize='100px' src='/images/icon1.png' />
          </Center>
          <Text fontSize='25px'>アカウント作成</Text>
          <HStack spacing="-12">
            <FormControl>
              <FormLabel htmlFor='lastname' fontSize='15px' mx={"10"} mt={"5"} >姓</FormLabel>
              <Input id='lastname' borderColor='#0A89FF' w='60%' h='30px' mx={"10"}/>
            </FormControl>
            <FormControl>
              <FormLabel htmlFor='lastname' fontSize='15px' mx={"10"} mt={"5"}>名</FormLabel>
              <Input id='firstname' borderColor='#0A89FF' w='60%' h='30px' mx={"10"} />
            </FormControl>
          </HStack>
          <FormControl>
            <FormLabel htmlFor='lastname' fontSize='15px' mx={"10"} mt={"5"}>メールアドレス</FormLabel>
            <Input id='email' borderColor='#0A89FF' w='77%' h='30px' mx={"10"} />
          </FormControl>
          <HStack spacing="-12">
            <FormControl>
              <FormLabel htmlFor='password' fontSize='15px' mx={"10"} mt={"5"} >パスワード</FormLabel>
              <Input id='password' borderColor='#0A89FF' w='60%' h='30px' mx={"10"}/>
            </FormControl>
            <FormControl>
              <FormLabel htmlFor='confirmation' fontSize='15px' mx={"10"} mt={"5"}>確認</FormLabel>
              <Input id='confirmation' borderColor='#0A89FF' w='60%' h='30px' mx={"10"} />
            </FormControl>
          </HStack>
          <HStack spacing="10" mt={"12"}>
          <Button color='#0A89FF' background='#FFFFFF' w='150px' h='40px' mx={"6"} >代わりにログイン</Button>
          <Button color='white' background='#0A89FF' w='100px' h='40px' >登録</Button>
          </HStack>
        </Box>   
       </Box>
     </Center>
   </ChakraProvider>
  )
}